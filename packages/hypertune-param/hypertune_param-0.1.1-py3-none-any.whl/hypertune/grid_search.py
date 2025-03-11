# hypertune/grid_search.py

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer

class GridSearch:
    def __init__(self, model, param_grid, scoring="accuracy"):
        self.model = model
        self.param_grid = param_grid
        self.scoring = scoring

    def optimize(self):
        grid_search = GridSearchCV(estimator=self.model,
                                   param_grid=self.param_grid,
                                   scoring=self.scoring,
                                   n_jobs=-1,
                                   cv=5)  

        grid_search.fit(X_train, y_train)
        best_params = grid_search.best_params_
        best_score = grid_search.best_score_

        return best_params, best_score
