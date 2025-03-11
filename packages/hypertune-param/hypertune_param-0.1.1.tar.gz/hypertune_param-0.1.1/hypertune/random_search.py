# hypertune/random_search.py

from sklearn.model_selection import RandomizedSearchCV
import numpy as np

class RandomSearch:
    def __init__(self, model, param_grid, n_iter=10, scoring="accuracy"):
        self.model = model
        self.param_grid = param_grid
        self.n_iter = n_iter
        self.scoring = scoring

    def optimize(self):
        random_search = RandomizedSearchCV(estimator=self.model,
                                           param_distributions=self.param_grid,
                                           n_iter=self.n_iter,
                                           scoring=self.scoring,
                                           n_jobs=-1,
                                           cv=5,  
                                           random_state=42) 

        random_search.fit(X_train, y_train)
        best_params = random_search.best_params_
        best_score = random_search.best_score_

        return best_params, best_score
