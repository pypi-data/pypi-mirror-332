# tests/test_grid_search.py

import unittest
from sklearn.ensemble import RandomForestClassifier
from hypertune.grid_search import GridSearch

class TestGridSearch(unittest.TestCase):

    def setUp(self):
        """
        Setup for Grid Search tests. Initializes the model and parameter grid.
        """
        self.model = RandomForestClassifier(random_state=42)
        self.param_grid = {
            'n_estimators': [10, 50, 100],
            'max_depth': [5, 10, None]
        }

    def test_grid_search_basic(self):
        """
        Test basic functionality of GridSearch with the RandomForest model.
        """
        grid_search = GridSearch(self.model, self.param_grid)
        best_params, best_score = grid_search.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_grid_search_with_custom_metric(self):
        """
        Test GridSearch with a custom scoring metric (e.g., "f1" score).
        """
        from sklearn.metrics import f1_score
        grid_search = GridSearch(self.model, self.param_grid, scoring="f1")
        best_params, best_score = grid_search.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_grid_search_invalid_param_grid(self):
        """
        Test GridSearch with an invalid parameter grid.
        """
        invalid_param_grid = {
            'n_estimators': [10, -50, 100],
            'max_depth': [5, 'ten', None]
        }
        grid_search = GridSearch(self.model, invalid_param_grid)

        with self.assertRaises(ValueError):
            grid_search.optimize()

if __name__ == '__main__':
    unittest.main()
