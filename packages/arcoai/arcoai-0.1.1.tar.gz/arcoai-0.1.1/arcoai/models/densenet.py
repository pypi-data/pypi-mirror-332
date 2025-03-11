import tensorflow as tf
from tensorflow.keras import layers, Model
import torch
import torch.nn as nn
import torch.optim as optim

class DenseNet:
    def __init__(self, input_shape, num_classes, backend_type='tensorflow'):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.backend_type = backend_type

    def create_model(self):
        if self.backend_type == 'tensorflow':
            return self._create_densenet_tensorflow()
        elif self.backend_type == 'pytorch':
            return self._create_densenet_pytorch()
        else:
            raise ValueError("Unsupported backend type")

    def _create_densenet_tensorflow(self):
        input_layer = layers.Input(shape=self.input_shape)
        
        x = layers.Conv2D(64, (3, 3), padding="same", activation="relu")(input_layer)
        x = layers.BatchNormalization()(x)
        x = layers.MaxPooling2D((2, 2))(x)
        
        x = self._dense_block(x, 64)
        x = self._dense_block(x, 128)
        
        x = layers.GlobalAveragePooling2D()(x)
        x = layers.Dense(128, activation="relu")(x)
        output_layer = layers.Dense(self.num_classes, activation="softmax")(x)
        
        model = Model(inputs=input_layer, outputs=output_layer)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def _create_densenet_pytorch(self):
        class DenseNet(nn.Module):
            def __init__(self):
                super(DenseNet, self).__init__()
                self.conv1 = nn.Conv2d(3, 64, kernel_size=3, padding=1)
                self.bn1 = nn.BatchNorm2d(64)
                self.pool = nn.MaxPool2d(2, 2)
                
                self.dense_block1 = self._dense_block(64, 128)
                self.dense_block2 = self._dense_block(128, 256)
                
                self.fc1 = nn.Linear(256, 128)
                self.fc2 = nn.Linear(128, self.num_classes)
                self.relu = nn.ReLU()
                self.softmax = nn.Softmax(dim=1)
                
            def _dense_block(self, in_channels, out_channels):
                layers = []
                layers.append(nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1))
                layers.append(nn.BatchNorm2d(out_channels))
                layers.append(nn.ReLU())
                layers.append(nn.Conv2d(out_channels, out_channels, kernel_size=3, padding=1))
                layers.append(nn.BatchNorm2d(out_channels))
                layers.append(nn.ReLU())
                return nn.Sequential(*layers)
                
            def forward(self, x):
                x = self.relu(self.bn1(self.conv1(x)))
                x = self.pool(x)
                x = self.dense_block1(x)
                x = self.dense_block2(x)
                x = x.view(x.size(0), -1)  # Flatten
                x = self.fc1(x)
                x = self.fc2(x)
                return self.softmax(x)
        
        return DenseNet()
