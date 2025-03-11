# tests/test_hypertune.py

import unittest
from sklearn.ensemble import RandomForestClassifier
from hypertune import Hypertune
from hypertune.grid_search import GridSearch
from hypertune.random_search import RandomSearch
from hypertune.bayesian_search import BayesianSearch

class TestHypertune(unittest.TestCase):

    def setUp(self):
        """
        Setup for Hypertune tests. Initializes the model and parameter grid/space.
        """
        self.model = RandomForestClassifier(random_state=42)
        self.param_grid = {
            'n_estimators': [10, 50, 100],
            'max_depth': [5, 10, None]
        }
        self.param_space = {
            'n_estimators': [10, 50, 100],
            'max_depth': [5, 10, None]
        }

    def test_hypertune_with_grid_search(self):
        """
        Test Hypertune with GridSearch as the optimization method.
        """
        hypertune = Hypertune(self.model, search_method=GridSearch, param_grid=self.param_grid)
        best_params, best_score = hypertune.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_hypertune_with_random_search(self):
        """
        Test Hypertune with RandomSearch as the optimization method.
        """
        hypertune = Hypertune(self.model, search_method=RandomSearch, param_grid=self.param_grid, n_iter=5)
        best_params, best_score = hypertune.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_hypertune_with_bayesian_search(self):
        """
        Test Hypertune with BayesianSearch as the optimization method.
        """
        hypertune = Hypertune(self.model, search_method=BayesianSearch, param_space=self.param_space, n_iter=5)
        best_params, best_score = hypertune.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_hypertune_invalid_search_method(self):
        """
        Test Hypertune with an invalid search method.
        """
        with self.assertRaises(ValueError):
            Hypertune(self.model, search_method="InvalidMethod", param_grid=self.param_grid)

if __name__ == '__main__':
    unittest.main()
