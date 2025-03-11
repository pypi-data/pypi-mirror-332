import pytest
import numpy as np
from arcoai.models import DenseNet
from arcoai.datasets import DatasetLoader

def test_densenet_creation():
    model = DenseNet(input_shape=(224, 224, 3), num_classes=10, backend_type='tensorflow')
    assert model is not None
    assert model.input_shape == (224, 224, 3)
    assert model.num_classes == 10

def test_densenet_training():
    dataset = DatasetLoader(backend_type='tensorflow').load_dataset(data_dir='path_to_data', batch_size=32)
    model = DenseNet(input_shape=(224, 224, 3), num_classes=10, backend_type='tensorflow')
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    history = model.fit(dataset, epochs=1)
    assert history.history['accuracy'][0] > 0.0

def test_densenet_evaluation():
    dataset = DatasetLoader(backend_type='tensorflow').load_dataset(data_dir='path_to_test_data', batch_size=32)
    model = DenseNet(input_shape=(224, 224, 3), num_classes=10, backend_type='tensorflow')
    test_loss, test_acc = model.evaluate(dataset)
    assert test_acc >= 0.0
