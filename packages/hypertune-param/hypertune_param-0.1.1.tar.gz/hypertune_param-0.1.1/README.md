# Hypertune

Hypertune is a Python library designed to simplify hyperparameter optimization for machine learning models. It supports different search strategies, including Grid Search, Random Search, and Bayesian Optimization, to find the best hyperparameters for your model and improve its performance.

Features

- **Grid Search**: Exhaustively searches through a manually specified grid of hyperparameters.
- **Random Search**: Randomly samples hyperparameter combinations to find optimal settings.
- **Bayesian Optimization**: Uses probabilistic models to predict the best hyperparameters and minimize the number of trials needed.

## Installation

You can install **Hypertune** using `pip` from PyPI:

```bash
pip install hypertune
```

## Usage

Here’s how to use **Hypertune** with a machine learning model:

### 1. Import the library

```python
from hypertune import Hypertune
from hypertune.grid_search import GridSearch
from hypertune.random_search import RandomSearch
from hypertune.bayesian_search import BayesianSearch
```

### 2. Define the model and parameters

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Load a dataset
X, y = load_iris(return_X_y=True)

# Define the model
model = RandomForestClassifier()

# Define hyperparameter search space for GridSearch
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 5, 10]
}
```

### 3. Run Grid Search

```python
# Create the GridSearch object
grid_search = GridSearch(model, param_grid)

# Fit the model and find the best parameters
grid_search.fit(X, y)

# Get the best hyperparameters
print("Best Hyperparameters:", grid_search.best_params_)
```

### 4. Run Random Search

```python
# Define the random search space
param_dist = {
    'n_estimators': [50, 100, 200, 300],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10, 15]
}

# Create the RandomSearch object
random_search = RandomSearch(model, param_dist)

# Fit the model and find the best parameters
random_search.fit(X, y)

# Get the best hyperparameters
print("Best Hyperparameters:", random_search.best_params_)
```

### 5. Run Bayesian Optimization

```python
# Define the hyperparameter search space for Bayesian Optimization
param_space = {
    'n_estimators': (50, 200),
    'max_depth': (1, 30),
    'min_samples_split': (2, 15)
}

# Create the BayesianSearch object
bayesian_search = BayesianSearch(model, param_space)

# Fit the model and find the best parameters
bayesian_search.fit(X, y)

# Get the best hyperparameters
print("Best Hyperparameters:", bayesian_search.best_params_)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
