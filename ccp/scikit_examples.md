# scikit-learn examples

![Scikit-learn logo](../images/scikit_logo.png)

## General example

We'll work on a classic problem: classifying flowers in the Iris dataset.

### Problem statement

The goal is to classify iris flowers into three species (Setosa, Versicolor, and Virginica) based on the length and width of their sepals and petals. We'll follow these steps:

1. **Load the dataset**
2. **Explore the data**
3. **Preprocess the data**
4. **Split the data into training and testing sets**
5. **Build and train a model**
6. **Make predictions**
7. **Evaluate the model**
8. **Tune hyperparameters**
9. **Visualize the results**

### Load the dataset

First, we'll load the Iris dataset, which is available directly in Scikit-learn.

```python
from sklearn.datasets import load_iris
import pandas as pd

# Load the dataset
iris = load_iris()

# Convert to a DataFrame for easier exploration
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
iris_df['species'] = iris.target
iris_df['species'] = iris_df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

print(iris_df.head())
```

### Explore the data

Understanding the data is crucial before proceeding. Let's check some basic statistics and visualize the relationships between features.

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Display basic statistics
print(iris_df.describe())

# Pairplot to visualize the relationships
sns.pairplot(iris_df, hue="species")
plt.show()
```

### Preprocess the data

Preprocessing often involves scaling features, handling missing values, or encoding categorical variables. In this case, the Iris dataset is already clean, but we'll scale the features for better model performance.

```python
from sklearn.preprocessing import StandardScaler

# Features (X) and labels (y)
X = iris.data
y = iris.target

# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### Split the data into training and testing datasets

We'll split the dataset into training and testing datasets to evaluate how well our model generalizes to unseen data.

```python
from sklearn.model_selection import train_test_split

# Split the data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print(f"Training set size: {X_train.shape[0]}")
print(f"Testing set size: {X_test.shape[0]}")
```

### Build and train a model

We'll start with a simple model, the k-nearest neighbors (KNN) classifier, which classifies data points based on the labels of their nearest neighbors.

```python
from sklearn.neighbors import KNeighborsClassifier

# Initialize the model with 3 neighbors
knn = KNeighborsClassifier(n_neighbors=3)

# Train the model
knn.fit(X_train, y_train)
```

### Make predictions

After training the model, we can use it to make predictions on the test set.

```python
# Predict the labels for the test set
y_pred = knn.predict(X_test)

print(f"Predictions: {y_pred}")
print(f"Actual labels: {y_test}")
```

### Evaluate the model

Evaluating the model helps us understand its performance. We can calculate accuracy, precision, recall and other metrics.

```python
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Detailed classification report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Confusion matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
```

### Hyperparameters tuning

To potentially improve the model, we can tune hyperparameters like the number of neighbors in KNN using GridSearchCV.

```python
from sklearn.model_selection import GridSearchCV

# Define the parameter grid
param_grid = {'n_neighbors': [1, 3, 5, 7, 9]}

# Initialize GridSearchCV
grid_search = GridSearchCV(KNeighborsClassifier(), param_grid, cv=5)

# Fit the model
grid_search.fit(X_train, y_train)

# Best parameters and accuracy
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation accuracy: {grid_search.best_score_ * 100:.2f}%")
```

### Visualize the results

Visualizing the model's performance can provide deeper insights. We can plot the decision boundaries or the confusion matrix.

```python
import numpy as np
import matplotlib.pyplot as plt

# Function to plot decision boundaries
def plot_decision_boundaries(X, y, model):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),
                         np.arange(y_min, y_max, 0.01))
    
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    plt.contourf(xx, yy, Z, alpha=0.4)
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolor='k')
    plt.show()

# Reduce the dataset to 2 features for visualization
X_reduced = X_train[:, :2]
model_reduced = KNeighborsClassifier(n_neighbors=3)
model_reduced.fit(X_reduced, y_train)

# Plot decision boundaries
plot_decision_boundaries(X_reduced, y_train, model_reduced)
```

In this example, we've walked through the process of building, training, and evaluating a KNN classifier on the Iris dataset using Scikit-learn. We also explored hyperparameter tuning and visualized the results. This workflow is typical for many machine learning tasks and can be adapted to more complex datasets and models.


## FAIRiCUBE examples