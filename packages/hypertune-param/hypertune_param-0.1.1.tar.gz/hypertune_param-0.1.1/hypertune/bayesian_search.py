# hypertune/bayesian_search.py

from hyperopt import fmin, tpe, hp, Trials
from sklearn.metrics import make_scorer

class BayesianSearch:
    def __init__(self, model, param_space, n_iter=10, scoring="accuracy"):
        self.model = model
        self.param_space = param_space
        self.n_iter = n_iter
        self.scoring = scoring
        self.best_params = None
        self.best_score = None

    def optimize(self):
        trials = Trials()

        def objective(params):
            self.model.set_params(**params)
            self.model.fit(X_train, y_train)  
            score = self.model.score(X_val, y_val)  
            return {'loss': -score, 'status': 'ok'}
        best = fmin(fn=objective,
                    space=self.param_space,
                    algo=tpe.suggest,
                    max_evals=self.n_iter,
                    trials=trials)

        self.best_params = best
        self.best_score = -trials.best_trial['result']['loss'] 
        return self.best_params, self.best_score
