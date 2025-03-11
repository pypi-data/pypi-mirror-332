# ArcoAI - Simple Deep Learning Library

ArcoAI is a deep learning library simplifying the process of creating and training neural networks (ANNs and CNNs). The library provides pre-built models like DenseNet, ResNet, and VGG, and tools to easily load datasets and configure training pipelines for both TensorFlow and PyTorch backends.

## Installation

To install ArcoAI, simply run:

```bash
pip install arcoai
```

## Getting Started

### 1. Importing Models

You can easily import pre-built models like DenseNet, ResNet, and VGG:

```python
from arcoai.models import DenseNet, ResNet, VGG
```

### 2. Creating a Model

To create a model, instantiate the class with the desired input shape, number of classes, and backend type (either 'tensorflow' or 'pytorch'):

```python
# For TensorFlow backend
model = DenseNet(input_shape=(224, 224, 3), num_classes=10, backend_type='tensorflow')

# For PyTorch backend
model = DenseNet(input_shape=(224, 224, 3), num_classes=10, backend_type='pytorch')
```

### 3. Loading a Dataset

To load datasets, use the `DatasetLoader` class. You can specify the backend type, image size, and batch size:

```python
from arcoai.datasets import DatasetLoader

# For TensorFlow backend
dataset = DatasetLoader(backend_type='tensorflow').load_dataset(data_dir='path_to_data')

# For PyTorch backend
dataset = DatasetLoader(backend_type='pytorch').load_dataset(data_dir='path_to_data', batch_size=32)
```

### 4. Training the Model

Once the model and dataset are ready, you can train the model using TensorFlow's or PyTorch's training functions. For TensorFlow:

```python
model.fit(dataset, epochs=10)
```

For PyTorch:

```python
import torch.optim as optim

optimizer = optim.Adam(model.parameters(), lr=0.001)
criterion = torch.nn.CrossEntropyLoss()

# Training loop
for epoch in range(10):
    for data, target in dataset:
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()
```

## Models

ArcoAI provides the following pre-built models:

- **DenseNet**: A deep convolutional network that uses dense connections between layers.
- **ResNet**: A deep residual network that allows training of very deep networks with skip connections.
- **VGG**: A simple yet effective convolutional network architecture with multiple convolutional layers.
