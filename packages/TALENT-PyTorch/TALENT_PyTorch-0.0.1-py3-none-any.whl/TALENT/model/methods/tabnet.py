from TALENT.model.methods.base import Method
import torch
import torch
import torch.nn.functional as F

from TALENT.model.lib.data import (
    Dataset,
    data_nan_process,
    data_enc_process,
    num_enc_process,
    data_norm_process,
    data_label_process
)
import time

class TabNetMethod(Method):
    def __init__(self, args, is_regression):
        super().__init__(args, is_regression)
        assert(args.cat_policy != 'indices')

    def construct_model(self, model_config = None):
        from TALENT.model.models.tabnet import TabNetClassifier, TabNetRegressor
        if model_config is None:
            model_config = self.args.config['model']
        if self.is_regression:
            self.model = TabNetRegressor(
                gamma=model_config['gamma'],
                n_steps=model_config['n_steps'],
                n_independent=model_config['n_independent'],
                n_shared=model_config['n_shared'],
                momentum=model_config['momentum'],
                optimizer_params={'lr':model_config['lr']},
                seed=self.args.seed)
        else:
            self.model = TabNetClassifier(
                gamma=model_config['gamma'],
                n_steps=model_config['n_steps'],
                n_independent=model_config['n_independent'],
                n_shared=model_config['n_shared'],
                momentum=model_config['momentum'],
                optimizer_params={'lr':model_config['lr']},
                seed=self.args.seed)
            
    def data_format(self, is_train = True, N = None, C = None, y = None):
        if is_train:
            self.N, self.C, self.num_new_value, self.imputer, self.cat_new_value = data_nan_process(self.N, self.C, self.args.num_nan_policy, self.args.cat_nan_policy)
            self.y, self.y_info, self.label_encoder = data_label_process(self.y, self.is_regression)
            self.N,self.num_encoder = num_enc_process(self.N,num_policy = self.args.num_policy, n_bins = self.args.config['training']['n_bins'],y_train=self.y['train'],is_regression=self.is_regression)
            self.N, self.C, self.ord_encoder, self.mode_values, self.cat_encoder = data_enc_process(self.N, self.C, self.args.cat_policy, self.y['train'])
            self.N, self.normalizer = data_norm_process(self.N, self.args.normalization, self.args.seed)
        else:
            N_test, C_test, _, _, _ = data_nan_process(N, C, self.args.num_nan_policy, self.args.cat_nan_policy, self.num_new_value, self.imputer, self.cat_new_value)
            y_test, _, _ = data_label_process(y, self.is_regression, self.y_info, self.label_encoder)
            N_test,_ = num_enc_process(N_test,num_policy=self.args.num_policy,n_bins = self.args.config['training']['n_bins'],y_train=None,encoder = self.num_encoder)
            N_test, C_test, _, _, _ = data_enc_process(N_test, C_test, self.args.cat_policy, None, self.ord_encoder, self.mode_values, self.cat_encoder)
            N_test, _ = data_norm_process(N_test, self.args.normalization, self.args.seed, self.normalizer)
            if N_test is not None and C_test is not None:
                self.N_test,self.C_test = N_test['test'],C_test['test']
            elif N_test is None and C_test is not None:
                self.N_test,self.C_test = None,C_test['test']
            else:
                self.N_test,self.C_test = N_test['test'],None
            self.y_test = y_test['test']
        self.criterion = F.cross_entropy if not self.is_regression else F.mse_loss

    def fit(self, data, info, train = True, config = None):
        N,C,y = data
        # if the method already fit the dataset, skip these steps (such as the hyper-tune process)
        self.D = Dataset(N, C, y, info)
        self.N, self.C, self.y = self.D.N, self.D.C, self.D.y
        self.is_binclass, self.is_multiclass, self.is_regression = self.D.is_binclass, self.D.is_multiclass, self.D.is_regression
        self.n_num_features, self.n_cat_features = self.D.n_num_features, self.D.n_cat_features
        
        if config is not None:
            self.reset_stats_withconfig(config)
        self.data_format(is_train = True)
        self.construct_model()
        # if not train, skip the training process. such as load the checkpoint and directly predict the results
        if not train:
            return
        X_train = self.N['train']
        y_train = self.y['train']
        X_valid = self.N['val']
        y_valid = self.y['val']
        eval_metric = ['accuracy']
        if self.is_regression:
            y_train = y_train.reshape(-1, 1)
            y_valid = y_valid.reshape(-1, 1)
            eval_metric = ['rmse']
            task = "regression"
        elif self.is_binclass:
            task = "binclass"
        else:
            task = "multiclass"
        tic = time.time()
        loss, result, auc = self.model.fit(
            X_train=X_train, y_train=y_train,
            eval_set=[(X_valid, y_valid)],
            eval_name=['valid'],
            eval_metric=eval_metric,
            max_epochs=self.args.max_epoch, patience=20,
            batch_size=self.args.batch_size, virtual_batch_size=256,
            device=f'cuda:0',
            task=task
        )
        time_cost = time.time() - tic
        self.model.save_model(self.args.save_path)
        self.trlog['best_res'] = self.model.best_cost
        if self.is_regression:
            self.trlog['best_res'] = self.model.best_cost * self.y_info['std']
        return time_cost
    
    def predict(self, data, info, model_name):
        N,C,y = data
        self.model.load_model(self.args.save_path,self.args.seed)
        self.data_format(False, N, C, y)
        if self.is_regression:
            task_type = "regression"
            test_logit = self.model.predict(self.N_test)
        else:
            task_type = "classification"
            test_logit = self.model.predict_proba(self.N_test)
        test_label = self.y_test
        vl = self.criterion(torch.tensor(test_logit), torch.tensor(test_label)).item()     

        vres, metric_name = self.metric(test_logit, test_label, self.y_info)

        print('Test: loss={:.4f}'.format(vl))
        for name, res in zip(metric_name, vres):
            print('[{}]={:.4f}'.format(name, res))

        
        return vl, vres, metric_name, test_logit
