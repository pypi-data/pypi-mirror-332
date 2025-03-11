# tests/test_random_search.py

import unittest
from sklearn.ensemble import RandomForestClassifier
from hypertune.random_search import RandomSearch

class TestRandomSearch(unittest.TestCase):

    def setUp(self):
        """
        Setup for Random Search tests. Initializes the model and parameter grid.
        """
        self.model = RandomForestClassifier(random_state=42)
        self.param_grid = {
            'n_estimators': [10, 50, 100],
            'max_depth': [5, 10, None]
        }

    def test_random_search_basic(self):
        """
        Test basic functionality of RandomSearch with the RandomForest model.
        """
        random_search = RandomSearch(self.model, self.param_grid, n_iter=5)
        best_params, best_score = random_search.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_random_search_with_custom_metric(self):
        """
        Test RandomSearch with a custom scoring metric (e.g., "f1" score).
        """
        from sklearn.metrics import f1_score
        random_search = RandomSearch(self.model, self.param_grid, n_iter=5, scoring="f1")
        best_params, best_score = random_search.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_random_search_invalid_param_grid(self):
        """
        Test RandomSearch with an invalid parameter grid.
        """
        invalid_param_grid = {
            'n_estimators': [10, -50, 100],
            'max_depth': [5, 'ten', None]
        }
        random_search = RandomSearch(self.model, invalid_param_grid, n_iter=5)

        with self.assertRaises(ValueError):
            random_search.optimize()

if __name__ == '__main__':
    unittest.main()
