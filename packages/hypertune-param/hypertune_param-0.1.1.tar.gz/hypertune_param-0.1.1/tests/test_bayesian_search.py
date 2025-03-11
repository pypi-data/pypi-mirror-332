# tests/test_bayesian_search.py

import unittest
from sklearn.ensemble import RandomForestClassifier
from hypertune.bayesian_search import BayesianSearch
from hyperopt import hp

class TestBayesianSearch(unittest.TestCase):

    def setUp(self):
        """
        Setup for Bayesian Search tests. Initializes the model and parameter space.
        """
        self.model = RandomForestClassifier(random_state=42)
        self.param_space = {
            'n_estimators': hp.choice('n_estimators', [10, 50, 100]),
            'max_depth': hp.choice('max_depth', [5, 10, None])
        }

    def test_bayesian_search_basic(self):
        """
        Test basic functionality of BayesianSearch with the RandomForest model.
        """
        bayesian_search = BayesianSearch(self.model, self.param_space, n_iter=5)
        best_params, best_score = bayesian_search.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_bayesian_search_with_custom_metric(self):
        """
        Test BayesianSearch with a custom scoring metric (e.g., "f1" score).
        """
        from sklearn.metrics import f1_score
        bayesian_search = BayesianSearch(self.model, self.param_space, n_iter=5, scoring="f1")
        best_params, best_score = bayesian_search.optimize()

        self.assertIsInstance(best_params, dict)
        self.assertGreater(best_score, 0)
        self.assertIn('n_estimators', best_params)
        self.assertIn('max_depth', best_params)

    def test_bayesian_search_invalid_param_space(self):
        """
        Test BayesianSearch with an invalid parameter space.
        """
        invalid_param_space = {
            'n_estimators': hp.choice('n_estimators', [10, -50, 100]),
            'max_depth': hp.choice('max_depth', [5, 'ten', None])
        }
        bayesian_search = BayesianSearch(self.model, invalid_param_space, n_iter=5)

        with self.assertRaises(ValueError):
            bayesian_search.optimize()

if __name__ == '__main__':
    unittest.main()
