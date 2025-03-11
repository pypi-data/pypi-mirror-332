import pytest
import torch
import tensorflow as tf
from arcoai.models import DenseNet, ResNet
from arcoai.datasets import DatasetLoader

def test_tensorflow_training():
    dataset = DatasetLoader(backend_type='tensorflow').load_dataset(data_dir='path_to_data', batch_size=32)
    model = DenseNet(input_shape=(224, 224, 3), num_classes=10, backend_type='tensorflow')
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(dataset, epochs=1)
    assert history.history['accuracy'][0] > 0.0

def test_pytorch_training():
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
