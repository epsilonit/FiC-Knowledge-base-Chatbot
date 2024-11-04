# Getting Started with scikit-learn

![Scikit-learn logo](../images/scikit_logo.png)

Getting started with Scikit-learn is an exciting journey into the world of machine learning, where you can leverage this powerful Python library to build, train and evaluate machine learning models. Scikit-learn, also known as sklearn, is an open-source library that provides simple and efficient tools for data mining and data analysis. It is built on top of NumPy, SciPy and Matplotlib, making it easy to integrate with other popular scientific computing libraries in Python.

## Installation

Before diving into Scikit-learn, you'll need to install it in your Python environment. Scikit-learn can be installed via pip or Anaconda.

### Using pip
To install Scikit-learn using pip, simply run:

```bash
pip install scikit-learn
```

This command installs the latest version of Scikit-learn along with its dependencies.

### Using Anaconda
If you prefer using Anaconda, you can install Scikit-learn with:

```bash
conda install scikit-learn
```

This will install Scikit-learn in your Anaconda environment, ensuring compatibility with other scientific computing packages.

## Understanding the basics

Scikit-learn is built around the concept of estimators, which are objects that implement machine learning algorithms. These estimators are used for tasks like classification, regression, clustering and dimensionality reduction. The core components of Scikit-learn include:

- **Datasets**: Scikit-learn provides several sample datasets that are useful for practice and experimentation.
- **Preprocessing**: Tools for preprocessing data, including scaling, normalization and encoding categorical variables.
- **Model Selection**: Functions for splitting datasets, cross-validation and hyperparameter tuning.
- **Metrics**: A wide range of metrics for evaluating model performance.

## Loading and preparing data

Scikit-learn provides several built-in datasets for practice, such as the Iris dataset, which contains measurements of different iris flowers. You can load these datasets using Scikit-learn's `datasets` module.

### Loading a dataset
Here's how to load the Iris dataset:

```python
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
X, y = iris.data, iris.target

print(f"Features: {X[:5]}")
print(f"Labels: {y[:5]}")
```

- **X**: The feature matrix, where each row represents an instance and each column represents a feature.
- **y**: The target vector, where each element corresponds to the class label of the instance.

### Splitting the dataset
Before training a model, it is common practice to split the data into training and testing sets. This allows you to evaluate the model's performance on unseen data.

```python
from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape}")
print(f"Testing set size: {X_test.shape}")
```

## Preprocessing the data

Preprocessing is a crucial step in machine learning, as it prepares the data for modeling. Scikit-learn provides several tools for preprocessing, such as scaling features, handling missing values and encoding categorical variables.

### Feature scaling
Many machine learning algorithms perform better when features are scaled. Scikit-learn's `StandardScaler` standardizes features by removing the mean and scaling to unit variance.

```python
from sklearn.preprocessing import StandardScaler

# Initialize the scaler
scaler = StandardScaler()

# Fit the scaler to the training data and transform it
X_train_scaled = scaler.fit_transform(X_train)

# Transform the test data
X_test_scaled = scaler.transform(X_test)
```

## Building and training a model

Scikit-learn makes it easy to build and train models with its simple and consistent API. For example, let's build a k-nearest neighbors (KNN) classifier.

### Choosing an estimator
First, choose an estimator that fits the problem. For a classification task like the Iris dataset, a KNN classifier can be a good choice.

```python
from sklearn.neighbors import KNeighborsClassifier

# Initialize the model
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train_scaled, y_train)
```

- **n_neighbors**: The number of neighbors to consider when making a classification decision.

## Making predictions and evaluating the model

After training the model, you can use it to make predictions on new data and evaluate its performance.

### Making predictions
To make predictions on the test set:

```python
y_pred = knn.predict(X_test_scaled)
print(f"Predicted labels: {y_pred[:5]}")
```

### Evaluating the model
Scikit-learn provides various metrics for evaluating model performance. For classification tasks, accuracy is one of the most straightforward metrics.

```python
from sklearn.metrics import accuracy_score

# Calculate the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")
```

You can also generate a more detailed classification report, which includes precision, recall, and F1-score.

```python
from sklearn.metrics import classification_report

# Generate a classification report
report = classification_report(y_test, y_pred, target_names=iris.target_names)
print(report)
```

## Model selection and hyperparameter tuning

To improve model performance, you may need to try different models or adjust hyperparameters. Scikit-learn provides tools for cross-validation and hyperparameter tuning.

### Cross-Validation
Cross-validation helps you evaluate how well your model generalizes to new data by splitting the data into multiple folds and training/testing the model on each fold.

```python
from sklearn.model_selection import cross_val_score

# Perform cross-validation
cv_scores = cross_val_score(knn, X_train_scaled, y_train, cv=5)

print(f"Cross-validation scores: {cv_scores}")
print(f"Mean cross-validation score: {cv_scores.mean()}")
```

### Hyperparameter tuning
You can use grid search to find the best hyperparameters for your model:

```python
from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {'n_neighbors': [3, 5, 7, 9]}

# Initialize grid search
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)

# Fit the model
grid_search.fit(X_train_scaled, y_train)

# Get the best parameters
best_params = grid_search.best_params_
print(f"Best parameters: {best_params}")
```

## Saving and loading models

After finding the best model, you can save it for future use. Scikit-learn models can be saved using Python's `pickle` or `joblib` libraries.

```python
import joblib

# Save the model
joblib.dump(knn, 'knn_model.pkl')

# Load the model
loaded_model = joblib.load('knn_model.pkl')

# Use the loaded model to make predictions
y_pred_loaded = loaded_model.predict(X_test_scaled)
```
