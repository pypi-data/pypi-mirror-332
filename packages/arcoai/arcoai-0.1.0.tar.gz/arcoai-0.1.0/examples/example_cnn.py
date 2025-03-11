import torch
import torch.nn as nn
import torch.optim as optim
from arcoai.models import ResNet
from arcoai.datasets import DatasetLoader
from torch.utils.data import DataLoader

# Load the dataset using the DatasetLoader
dataset = DatasetLoader(backend_type='pytorch').load_dataset(data_dir='path_to_data', batch_size=32)

# Initialize the model (ResNet in this case)
model = ResNet(input_shape=(224, 224, 3), num_classes=10, backend_type='pytorch')

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
num_epochs = 10
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for data, target in dataset:
        optimizer.zero_grad()
        outputs = model(data)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {running_loss/len(dataset)}, Accuracy: {100 * correct / total}%")

# Save the model
torch.save(model.state_dict(), 'resnet_model.pth')

# Evaluate the model
test_dataset = DatasetLoader(backend_type='pytorch').load_dataset(data_dir='path_to_test_data', batch_size=32)
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for data, target in test_dataset:
        outputs = model(data)
        _, predicted = torch.max(outputs.data, 1)
        total += target.size(0)
        correct += (predicted == target).sum().item()

print(f"Test Accuracy: {100 * correct / total}%")
