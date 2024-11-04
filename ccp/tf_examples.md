# TensorFlow examples

![TensorFlow logo](../images/tf_logo.png)

## General example

In this example, we will create, train, and evaluate a neural network model on the MNIST dataset, which is a classic dataset of handwritten digits.

### Problem statement

The task is to classify handwritten digits (0-9) from the MNIST dataset. The dataset consists of 60,000 training images and 10,000 test images, each of size 28x28 pixels. Our goal is to build a neural network model that can accurately predict the digit represented in each image.

### Setup and import libraries

First, we'll import the necessary libraries and modules.

```python
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import matplotlib.pyplot as plt
```

### Load and prepare the data

We'll load the MNIST dataset, which is available directly in TensorFlow and preprocess it by normalizing the pixel values.

```python
# Load the MNIST dataset
(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

# Normalize the pixel values to the range [0, 1]
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Reshape the data to fit the model input requirements
X_train = np.expand_dims(X_train, axis=-1)
X_test = np.expand_dims(X_test, axis=-1)

# Check the shape of the data
print(f"Training data shape: {X_train.shape}")
print(f"Test data shape: {X_test.shape}")
```

### Explore the data

It's good practice to visualize some of the data to get an understanding of what we're working with.

```python
# Plot a few examples from the training set
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.show()
```

### Build the model

We'll define a simple convolutional neural network (CNN) for this task. CNNs are particularly effective for image classification tasks.

```python
# Build the model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Print the model summary
model.summary()
```

### Compile the model

Next, we need to compile the model by specifying the loss function, optimizer and metrics for evaluation.

```python
# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

### Train the model

We'll train the model on the training data. We'll also include a validation split to monitor the model's performance on unseen data during training.

```python
# Train the model
history = model.fit(X_train, y_train, epochs=10, batch_size=64, validation_split=0.2)
```

### Evaluate the model

After training, we should evaluate the model on the test data to see how well it generalizes to new unseen data.

```python
# Evaluate the model on the test data
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"Test accuracy: {test_accuracy * 100:.2f}%")
```

### Visualize training history

TensorFlow's training history contains information about how the model's loss and accuracy changed over time. We can plot this to visualize the training process.

```python
# Plot training and validation accuracy
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')
plt.show()

# Plot training and validation loss
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()
```

### Make predictions

We can now use the trained model to make predictions on individual test images.

```python
# Predict the labels for test images
predictions = model.predict(X_test)

# Display a few predictions
plt.figure(figsize=(10, 10))
for i in range(9):
    plt.subplot(3, 3, i + 1)
    plt.imshow(X_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"True: {y_test[i]}, Predicted: {np.argmax(predictions[i])}")
    plt.axis('off')
plt.show()
```

### Save and Load the model

Finally, after training a successful model, you might want to save it for later use.

```python
# Save the model
model.save('mnist_cnn_model.h5')

# Load the model
loaded_model = tf.keras.models.load_model('mnist_cnn_model.h5')

# Confirm the model is working by evaluating on the test set
loaded_model.evaluate(X_test, y_test)
```

In this detailed example, we've walked through the process of building, training, and evaluating a convolutional neural network (CNN) using TensorFlow on the MNIST dataset. We've covered loading and preprocessing the data, building the model, compiling, training, evaluating and finally making predictions with the model. Additionally, we looked at how to visualize training progress and save/load the model for future use.

This example provides a strong foundation for working with TensorFlow on image classification tasks and the concepts can be extended to more complex datasets and architectures.


## FAIRiCUBE examples