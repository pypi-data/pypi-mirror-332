import tensorflow as tf
from tensorflow.keras import layers, Model
import torch
import torch.nn as nn

class VGG:
    def __init__(self, input_shape, num_classes, backend_type='tensorflow'):
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.backend_type = backend_type

    def create_model(self):
        if self.backend_type == 'tensorflow':
            return self._create_vgg_tensorflow()
        elif self.backend_type == 'pytorch':
            return self._create_vgg_pytorch()
        else:
            raise ValueError("Unsupported backend type")

    def _create_vgg_tensorflow(self):
        input_layer = layers.Input(shape=self.input_shape)

        x = self._vgg_block(x, 64, 2)
        x = self._vgg_block(x, 128, 2)
        x = self._vgg_block(x, 256, 3)
        x = self._vgg_block(x, 512, 3)
        x = self._vgg_block(x, 512, 3)

        x = layers.Flatten()(x)
        x = layers.Dense(4096, activation="relu")(x)
        x = layers.Dense(4096, activation="relu")(x)
        output_layer = layers.Dense(self.num_classes, activation="softmax")(x)

        model = Model(inputs=input_layer, outputs=output_layer)
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def _create_vgg_pytorch(self):
        class VGG(nn.Module):
            def __init__(self):
                super(VGG, self).__init__()
                self.features = self._make_layers([64, 64, 128, 128, 256, 256, 256, 512, 512, 512, 512, 512, 512])
                self.fc1 = nn.Linear(512 * 7 * 7, 4096)
                self.fc2 = nn.Linear(4096, 4096)
                self.fc3 = nn.Linear(4096, self.num_classes)
                self.relu = nn.ReLU()
                self.softmax = nn.Softmax(dim=1)

            def _make_layers(self, cfg):
                layers = []
                in_channels = 3
                for v in cfg:
                    layers.append(nn.Conv2d(in_channels, v, kernel_size=3, padding=1))
                    layers.append(nn.ReLU(inplace=True))
                    layers.append(nn.MaxPool2d(kernel_size=2, stride=2))
                    in_channels = v
                return nn.Sequential(*layers)

            def forward(self, x):
                x = self.features(x)
                x = x.view(x.size(0), -1)
                x = self.fc1(x)
                x = self.fc2(x)
                x = self.fc3(x)
                return self.softmax(x)

        return VGG()
    
    def _vgg_block(self, x, filters, num_convs):
        for _ in range(num_convs):
            x = layers.Conv2D(filters, (3, 3), padding="same", activation="relu")(x)
        x = layers.MaxPooling2D((2, 2), strides=(2, 2))(x)
        return x
