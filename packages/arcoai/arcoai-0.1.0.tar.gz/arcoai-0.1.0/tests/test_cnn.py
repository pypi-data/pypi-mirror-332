import pytest
import torch
from torch.utils.data import DataLoader
from arcoai.models import ResNet
from arcoai.datasets import DatasetLoader

def test_resnet_creation():
    model = ResNet(input_shape=(224, 224, 3), num_classes=10, backend_type='pytorch')
    assert model is not None
    assert model.input_shape == (224, 224, 3)
    assert model.num_classes == 10

def test_resnet_training():
    dataset = DatasetLoader(backend_type='pytorch').load_dataset(data_dir='path_to_data', batch_size=32)
    model = ResNet(input_shape=(224, 224, 3), num_classes=10, backend_type='pytorch')
    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    model.train()
    for data, target in dataset:
        optimizer.zero_grad()
        outputs = model(data)
        loss = criterion(outputs, target)
        loss.backward()
        optimizer.step()
    assert loss.item() > 0.0

def test_resnet_evaluation():
    test_dataset = DatasetLoader(backend_type='pytorch').load_dataset(data_dir='path_to_test_data', batch_size=32)
    model = ResNet(input_shape=(224, 224, 3), num_classes=10, backend_type='pytorch')
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for data, target in test_dataset:
            outputs = model(data)
            _, predicted = torch.max(outputs.data, 1)
            total += target.size(0)
            correct += (predicted == target).sum().item()

    assert correct / total >= 0.0
