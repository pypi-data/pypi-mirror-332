# **ArcoAI**

ArcoAI is a Python library that helps you easily build neural networks like ANNs and CNNs. It has simple tools that make it quick to create and customize models, whether you're just starting with deep learning or already know a lot about it. Plus, it includes cool features that help you understand how your models make decisions, like Grad-CAM, SmoothGrad, and Integrated Gradients.

## **Installation**

### 1. **Clone the repository**

You can either clone the repository using `git` or download it as a ZIP file.

```bash
git clone https://github.com/yourusername/arcoai.git
cd arcoai
```

### 2. **Create a virtual environment (Optional but recommended)**

To avoid conflicts with other packages, you can create a virtual environment for this project.

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. **Install dependencies**

Use `pip` to install all required dependencies listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```
## **Getting Started**

Once the package is installed, you can begin creating and training your own neural networks with just a few lines of code. Below are basic steps to get started with creating an ANN and CNN.

### **Example - Create and Train an ANN**

```python
from arcoai.models import ANN
from arcoai.datasets import load_dataset

# Load dataset (e.g., MNIST)
train_data, test_data = load_dataset('mnist')

# Initialize ANN model
model = ANN(input_size=784, hidden_layers=[128, 64], output_size=10)

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.train(train_data, epochs=10)

# Evaluate the model
accuracy = model.evaluate(test_data)
print(f"Test Accuracy: {accuracy}%")
```

### **Example - Create and Train a CNN**

```python
from arcoai.models import CNN
from arcoai.datasets import load_dataset

# Load dataset (e.g., CIFAR-10)
train_data, test_data = load_dataset('cifar10')

# Initialize CNN model
model = CNN(input_shape=(32, 32, 3), num_classes=10)

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.train(train_data, epochs=10)

# Evaluate the model
accuracy = model.evaluate(test_data)
print(f"Test Accuracy: {accuracy}%")
```

## **Model Architectures**

ArcoAI includes several pre-built architectures for quick experimentation with different types of models.

### **1. DenseNet**

DenseNet is a CNN architecture where each layer receives input from all previous layers. It's known for its high accuracy and efficiency in terms of parameters.

### **2. ResNet**

ResNet (Residual Network) is a deep CNN that uses skip connections, enabling the training of very deep models. This helps mitigate vanishing gradients.

### **3. VGG**

VGG is a CNN that consists of very deep layers with small 3x3 convolution filters. This architecture is popular for image classification tasks.

You can easily import and use these models from the `arcoai.models` package:

```python
from arcoai.models import ResNet, VGG, DenseNet
```

## **Visualization Tools**

ArcoAI comes with several powerful model interpretation tools (from Arcoson's gradientvis), which help visualize and understand the predictions made by your models.

### **1. Grad-CAM**

Grad-CAM (Gradient-weighted Class Activation Mapping) helps visualize which regions of an image were important for the model's prediction. 

```python
from arcoai.visualization import GradCAM

# Initialize GradCAM
gradcam = GradCAM(model, target_class=0)

# Generate heatmap
heatmap = gradcam.generate_heatmap(input_image)
gradcam.show_heatmap(heatmap)
```

### **2. SmoothGrad**

SmoothGrad is a technique to visualize the importance of different parts of an image by generating multiple noisy versions of the image.

```python
from arcoai.visualization import SmoothGrad

# Initialize SmoothGrad
smoothgrad = SmoothGrad(model)

# Generate noise-based visualization
visualization = smoothgrad.generate_visualization(input_image)
smoothgrad.show_visualization(visualization)
```

### **3. Integrated Gradients**

Integrated Gradients is a method that provides insights into the parts of an image that most influence the model's predictions.

```python
from arcoai.visualization import IntegratedGradients

# Initialize IntegratedGradients
integrated_gradients = IntegratedGradients(model)

# Compute attributions
attributions = integrated_gradients.compute_attributions(input_image)
integrated_gradients.show_attributions(attributions)
```

## **Examples**

You can find example scripts for both ANN and CNN in the `examples/` directory. These examples include basic training routines for MNIST, CIFAR-10, and other datasets.

To run an example:

```bash
python examples/example_ann.py
python examples/example_cnn.py
```

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
