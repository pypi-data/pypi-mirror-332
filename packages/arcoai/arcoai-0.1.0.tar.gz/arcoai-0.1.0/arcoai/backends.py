import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout, BatchNormalization
import torch
import torch.nn as nn
import torch.optim as optim

class Backend:
    def __init__(self, backend_type='tensorflow', framework_version='2.0'):
        self.backend_type = backend_type
        self.framework_version = framework_version

    def get_backend_info(self):
        return {
            "backend_type": self.backend_type,
            "framework_version": self.framework_version
        }

    def create_ANN(self, input_shape, layers, activation="relu", output_activation="softmax"):
        if self.backend_type == 'tensorflow':
            return self._create_ANN_tensorflow(input_shape, layers, activation, output_activation)
        elif self.backend_type == 'pytorch':
            return self._create_ANN_pytorch(input_shape, layers, activation, output_activation)
        else:
            raise ValueError("Unsupported backend type")

    def create_CNN(self, input_shape, conv_layers, dense_layers, activation="relu", output_activation="softmax"):
        if self.backend_type == 'tensorflow':
            return self._create_CNN_tensorflow(input_shape, conv_layers, dense_layers, activation, output_activation)
        elif self.backend_type == 'pytorch':
            return self._create_CNN_pytorch(input_shape, conv_layers, dense_layers, activation, output_activation)
        else:
            raise ValueError("Unsupported backend type")

    def _create_ANN_tensorflow(self, input_shape, layers, activation="relu", output_activation="softmax"):
        model = Sequential()
        model.add(Dense(layers[0], activation=activation, input_shape=(input_shape,)))
        
        for units in layers[1:]:
            model.add(Dense(units, activation=activation))
            model.add(BatchNormalization())
            model.add(Dropout(0.2))

        model.add(Dense(layers[-1], activation=output_activation))
        return model

    def _create_ANN_pytorch(self, input_shape, layers, activation="relu", output_activation="softmax"):
        class ANN(nn.Module):
            def __init__(self):
                super(ANN, self).__init__()
                self.layers = nn.ModuleList()
                self.layers.append(nn.Linear(input_shape, layers[0]))
                for units in layers[1:]:
                    self.layers.append(nn.Linear(units, units))
                    self.layers.append(nn.BatchNorm1d(units))
                    self.layers.append(nn.Dropout(0.2))
                self.output = nn.Linear(layers[-1], 10)  # Assume 10 output classes (change as needed)
                self.activation = nn.ReLU() if activation == "relu" else nn.Sigmoid()
                self.output_activation = nn.Softmax(dim=1) if output_activation == "softmax" else nn.Sigmoid()

            def forward(self, x):
                for layer in self.layers:
                    x = self.activation(layer(x))
                x = self.output(x)
                return self.output_activation(x)
        
        return ANN()

    def _create_CNN_tensorflow(self, input_shape, conv_layers, dense_layers, activation="relu", output_activation="softmax"):
        model = Sequential()
        
        for i, (filters, kernel_size, pool_size) in enumerate(conv_layers):
            if i == 0:
                model.add(Conv2D(filters, kernel_size, activation=activation, input_shape=input_shape))
            else:
                model.add(Conv2D(filters, kernel_size, activation=activation))
            model.add(BatchNormalization())
            model.add(MaxPooling2D(pool_size=pool_size))
            model.add(Dropout(0.25))
        
        model.add(Flatten())

        for units in dense_layers[:-1]:
            model.add(Dense(units, activation=activation))
            model.add(Dropout(0.5))

        model.add(Dense(dense_layers[-1], activation=output_activation))
        return model

    def _create_CNN_pytorch(self, input_shape, conv_layers, dense_layers, activation="relu", output_activation="softmax"):
        class CNN(nn.Module):
            def __init__(self):
                super(CNN, self).__init__()
                self.conv_layers = nn.ModuleList()
                for filters, kernel_size, pool_size in conv_layers:
                    self.conv_layers.append(nn.Conv2d(3, filters, kernel_size, padding=1))
                    self.conv_layers.append(nn.ReLU() if activation == "relu" else nn.Sigmoid())
                    self.conv_layers.append(nn.MaxPool2d(pool_size))
                    self.conv_layers.append(nn.Dropout(0.25))
                self.flatten = nn.Flatten()
                self.fc_layers = nn.ModuleList()
                in_features = input_shape[0] * input_shape[1] * input_shape[2]
                for units in dense_layers[:-1]:
                    self.fc_layers.append(nn.Linear(in_features, units))
                    self.fc_layers.append(nn.ReLU() if activation == "relu" else nn.Sigmoid())
                    self.fc_layers.append(nn.Dropout(0.5))
                    in_features = units
                self.fc_layers.append(nn.Linear(in_features, dense_layers[-1]))
                self.output_activation = nn.Softmax(dim=1) if output_activation == "softmax" else nn.Sigmoid()

            def forward(self, x):
                for layer in self.conv_layers:
                    x = layer(x)
                x = self.flatten(x)
                for layer in self.fc_layers:
                    x = layer(x)
                return self.output_activation(x)
        
        return CNN()
