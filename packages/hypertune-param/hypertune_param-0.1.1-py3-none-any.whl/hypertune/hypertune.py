# hypertune/hypertune.py

from .grid_search import GridSearch
from .random_search import RandomSearch
from .bayesian_search import BayesianSearch

class HyperTune:
    def __init__(self, model, param_grid=None, search_method="grid", n_iter=10, scoring="accuracy"):
        self.model = model
        self.param_grid = param_grid
        self.search_method = search_method
        self.n_iter = n_iter
        self.scoring = scoring

    def tune(self):

        if self.search_method == "grid":
            tuner = GridSearch(self.model, self.param_grid, self.scoring)
        elif self.search_method == "random":
            tuner = RandomSearch(self.model, self.param_grid, self.n_iter, self.scoring)
        elif self.search_method == "bayesian":
            tuner = BayesianSearch(self.model, self.param_grid, self.n_iter, self.scoring)
        else:
            raise ValueError("Invalid search method. Choose from 'grid', 'random', or 'bayesian'.")
        
        best_params, best_score = tuner.optimize()
        return best_params, best_score
