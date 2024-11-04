# Getting Started with PyTorch

![PyTorch logo](../images/pytorch_logo.webp)

Getting started with PyTorch involves understanding its fundamental concepts, setting up the environment and exploring its core functionalities. PyTorch is known for its dynamic computation graph, intuitive Pythonic interface and strong community support, making it an excellent choice for both beginners and experienced machine learning practitioners. This guide will walk you through the essentials of getting started with PyTorch, from installation to building your first neural network.

## Installation

Before you can start working with PyTorch, you need to install it in your environment. PyTorch can be installed on various platforms, including Windows, macOS and Linux. The installation process is straightforward and can be done using pip, conda or by building from source.

### Using pip
To install PyTorch using pip, you can run the following command in your terminal or command prompt:

```bash
pip install torch torchvision torchaudio
```

- **torch**: The core PyTorch package.
- **torchvision**: Provides tools for computer vision tasks, including datasets, model architectures, and image transformations.
- **torchaudio**: Offers tools for audio processing, commonly used in speech recognition and sound analysis.

### Using conda
If you're using Anaconda, you can install PyTorch with:

```bash
conda install pytorch torchvision torchaudio -c pytorch
```

The `-c pytorch` flag specifies the channel to pull the package from, ensuring you get the latest stable version of PyTorch.

### GPU support
PyTorch can take advantage of GPUs to accelerate computations. If you have a CUDA-enabled GPU, you can install a version of PyTorch with CUDA support:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

Replace `cu118` with the appropriate version for your CUDA toolkit. For conda, the installation is automatically configured based on your hardware.

## Understanding PyTorch Tensors

Tensors are the core data structure in PyTorch, similar to NumPy arrays but with additional capabilities like running on GPUs and supporting automatic differentiation. Tensors can be used to represent any kind of data—scalars, vectors, matrices, and even higher-dimensional data structures.

### Creating Tensors
You can create tensors in several ways:

```python
import torch

# Creating a tensor from a list
tensor_from_list = torch.tensor([1, 2, 3, 4])

# Creating a tensor of zeros
tensor_of_zeros = torch.zeros((2, 3))

# Creating a tensor of ones
tensor_of_ones = torch.ones((2, 3))

# Creating a random tensor
random_tensor = torch.rand((2, 3))
```

### Operations on Tensors
PyTorch supports a wide range of tensor operations, such as arithmetic operations, matrix multiplications and reshaping:

```python
# Element-wise addition
tensor_sum = tensor_of_ones + random_tensor

# Matrix multiplication
tensor_product = torch.mm(torch.rand(3, 3), torch.rand(3, 3))

# Reshaping a tensor
reshaped_tensor = tensor_of_zeros.view(3, 2)
```

## Automatic differentiation with Autograd

One of PyTorch’s most powerful features is `autograd`, its automatic differentiation engine. `autograd` records all operations performed on tensors that require gradients, enabling you to compute gradients easily for optimization during model training.

### Computing gradients
To compute gradients, you need to set `requires_grad=True` when creating a tensor:

```python
x = torch.tensor([2.0, 3.0], requires_grad=True)
y = x ** 2
y_sum = y.sum()

# Compute gradients
y_sum.backward()

# Gradients are now stored in the .grad attribute of x
print(x.grad)
```

In this example, PyTorch automatically computes the derivative of `y_sum` with respect to `x`, which is stored in `x.grad`.

## Building and training Neural Networks

PyTorch provides a high-level API through the `torch.nn` module for building and training neural networks. You can define models as subclasses of `nn.Module` and use predefined layers and activation functions.

### Defining a Neural Network
Here’s an example of a simple feedforward neural network for a classification task:

```python
import torch.nn as nn
import torch.nn.functional as F

class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        self.fc1 = nn.Linear(784, 128)  # Fully connected layer 1
        self.fc2 = nn.Linear(128, 64)   # Fully connected layer 2
        self.fc3 = nn.Linear(64, 10)    # Fully connected layer 3

    def forward(self, x):
        x = F.relu(self.fc1(x))  # Apply ReLU activation to layer 1
        x = F.relu(self.fc2(x))  # Apply ReLU activation to layer 2
        x = self.fc3(x)          # Output layer (no activation)
        return x

model = SimpleNet()
```

### Training the model
To train the model, you need to define a loss function and an optimizer. PyTorch provides several built-in loss functions (e.g., `CrossEntropyLoss`, `MSELoss`) and optimizers (e.g., `SGD`, `Adam`).

```python
import torch.optim as optim

# Loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
for epoch in range(10):
    optimizer.zero_grad()   # Zero the gradients
    output = model(input_data)  # Forward pass
    loss = criterion(output, target_data)  # Compute loss
    loss.backward()  # Backward pass
    optimizer.step()  # Update weights

    print(f'Epoch {epoch+1}, Loss: {loss.item()}')
```

## Data Handling with Datasets and DataLoaders

PyTorch provides utilities for loading and processing data efficiently through `torch.utils.data.Dataset` and `DataLoader`. These classes allow you to handle large datasets, perform batching, and apply data transformations.

### Custom dataset
Here’s an example of creating a custom dataset class:

```python
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# Sample data
data = torch.rand(100, 784)
labels = torch.randint(0, 10, (100,))

# Create Dataset and DataLoader
dataset = MyDataset(data, labels)
dataloader = DataLoader(dataset, batch_size=10, shuffle=True)
```

The `DataLoader` handles batching and shuffling, making it easier to iterate over the dataset during training.

## Model evaluation and saving

After training your model, you’ll want to evaluate its performance on a test set and save it for later use.

### Model evaluation
Switch the model to evaluation mode and test it:

```python
model.eval()  # Set the model to evaluation mode
correct = 0
total = 0
with torch.no_grad():  # Disable gradient calculation
    for data, labels in test_loader:
        outputs = model(data)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

print(f'Accuracy: {100 * correct / total}%')
```

### Saving and loading models
PyTorch allows you to save and load models easily:

```python
# Save the model
torch.save(model.state_dict(), 'model.pth')

# Load the model
model = SimpleNet()
model.load_state_dict(torch.load('model.pth'))
model.eval()
```

This process ensures that you can resume training or deploy the model in production environments.