# PyTorch examples

![PyTorch logo](../images/pytorch_logo.webp)

## General example

We will work on a regression task using the Boston Housing dataset. The goal will be to predict the median value of owner-occupied homes (in $1000s) based on various features.

### Problem statement

We will build a simple neural network to predict house prices using the Boston Housing dataset. The dataset contains 506 instances and 13 features, including variables such as crime rate, average number of rooms per dwelling and distance to employment centers.

### Setup and import libraries

First, we'll import the necessary libraries and modules.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset, random_split
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
```

### Load and prepare the data

We'll load the Boston Housing dataset and preprocess it by normalizing the features.

```python
# Load the Boston Housing dataset
boston = load_boston()
X, y = boston.data, boston.target

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convert to PyTorch tensors
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32).view(-1, 1)

# Create a TensorDataset and DataLoader
dataset = TensorDataset(X_tensor, y_tensor)

# Split the dataset into training and testing sets (80% train, 20% test)
train_size = int(0.8 * len(dataset))
test_size = len(dataset) - train_size
train_dataset, test_dataset = random_split(dataset, [train_size, test_size])

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
```

### Define the model

We'll create a simple feedforward neural network with one hidden layer.

```python
class SimpleRegressionModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(SimpleRegressionModel, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Initialize the model
input_dim = X_tensor.shape[1]
hidden_dim = 64
output_dim = 1

model = SimpleRegressionModel(input_dim, hidden_dim, output_dim)
```

### Define the loss function and optimizer

We'll use Mean Squared Error (MSE) as the loss function since this is a regression problem and Adam as the optimizer.

```python
# Define the loss function and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)
```

### Train the model

We'll train the model by iterating over the training dataset for a specified number of epochs.

```python
# Training the model
num_epochs = 100
train_losses = []

for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0.0
    
    for inputs, targets in train_loader:
        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        # Accumulate the loss for this epoch
        epoch_loss += loss.item() * inputs.size(0)

    # Calculate average loss for this epoch
    epoch_loss /= len(train_loader.dataset)
    train_losses.append(epoch_loss)
    
    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch + 1}/{num_epochs}], Loss: {epoch_loss:.4f}')
```

### Evaluate the model

After training, we should evaluate the model's performance on the test dataset.

```python
# Evaluate the model
model.eval()
test_loss = 0.0
with torch.no_grad():
    for inputs, targets in test_loader:
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        test_loss += loss.item() * inputs.size(0)

# Calculate average loss for the test set
test_loss /= len(test_loader.dataset)
print(f'Test Loss: {test_loss:.4f}')
```

### Visualize the training progress

We'll plot the training loss over epochs to visualize how well the model learned.

```python
# Plot training loss over epochs
plt.plot(train_losses, label='Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss Over Epochs')
plt.legend()
plt.show()
```

### Make predictions and visualize results

Finally, let's make predictions on the test dataset and compare them with the actual values.

```python
# Make predictions on the test set
model.eval()
predictions = []
actuals = []

with torch.no_grad():
    for inputs, targets in test_loader:
        outputs = model(inputs)
        predictions.extend(outputs.numpy())
        actuals.extend(targets.numpy())

predictions = np.array(predictions).flatten()
actuals = np.array(actuals).flatten()

# Plot predictions vs actual values
plt.scatter(actuals, predictions)
plt.plot([min(actuals), max(actuals)], [min(actuals), max(actuals)], color='red', lw=2)
plt.xlabel('Actual Prices ($1000s)')
plt.ylabel('Predicted Prices ($1000s)')
plt.title('Actual vs Predicted Prices')
plt.show()
```


In this detailed example, we've walked through the process of building, training and evaluating a simple feedforward neural network using PyTorch for a regression task. We've covered data loading, model definition, training, evaluation, and visualization.


## FAIRiCUBE examples

FAIRiCUBE Notebook Examples:

* [PyTorch Verification](https://github.com/FAIRiCUBE/common-code/blob/main/pytorch-verification/pytorch_verification.ipynb)

