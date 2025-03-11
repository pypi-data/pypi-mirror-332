import numpy as np
import tensorflow as tf
from arcoai.models import DenseNet
from arcoai.datasets import DatasetLoader
from tensorflow.keras.optimizers import Adam

# Load the dataset using the DatasetLoader
dataset = DatasetLoader(backend_type='tensorflow').load_dataset(data_dir='path_to_data', batch_size=32)

# Initialize the model (DenseNet in this case)
model = DenseNet(input_shape=(224, 224, 3), num_classes=10, backend_type='tensorflow')

# Compile the model
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(dataset, epochs=10)

# Save the model
model.save('densenet_model.h5')

# Evaluate the model
test_data = DatasetLoader(backend_type='tensorflow').load_dataset(data_dir='path_to_test_data', batch_size=32)
test_loss, test_acc = model.evaluate(test_data)
print(f"Test Accuracy: {test_acc}")
