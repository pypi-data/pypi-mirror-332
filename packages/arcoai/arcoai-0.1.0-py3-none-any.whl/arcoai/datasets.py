import tensorflow as tf
import torch
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from torch.utils.data import Dataset, DataLoader
import os
from PIL import Image
import numpy as np

class DatasetLoader:
    def __init__(self, backend_type='tensorflow'):
        self.backend_type = backend_type

    def load_dataset(self, data_dir, batch_size=32, image_size=(224, 224), shuffle=True):
        if self.backend_type == 'tensorflow':
            return self._load_tf_dataset(data_dir, batch_size, image_size, shuffle)
        elif self.backend_type == 'pytorch':
            return self._load_pytorch_dataset(data_dir, batch_size, image_size, shuffle)
        else:
            raise ValueError("Unsupported backend type")

    def _load_tf_dataset(self, data_dir, batch_size, image_size, shuffle):
        train_datagen = ImageDataGenerator(rescale=1./255, rotation_range=30, width_shift_range=0.2,
                                           height_shift_range=0.2, shear_range=0.2, zoom_range=0.2,
                                           horizontal_flip=True, fill_mode='nearest')

        train_generator = train_datagen.flow_from_directory(
            data_dir,
            target_size=image_size,
            batch_size=batch_size,
            class_mode='categorical',
            shuffle=shuffle)

        return train_generator

    def _load_pytorch_dataset(self, data_dir, batch_size, image_size, shuffle):
        class CustomDataset(Dataset):
            def __init__(self, data_dir, image_size):
                self.data_dir = data_dir
                self.image_size = image_size
                self.classes = os.listdir(data_dir)
                self.image_paths = []
                self.labels = []

                for idx, label in enumerate(self.classes):
                    label_path = os.path.join(data_dir, label)
                    if os.path.isdir(label_path):
                        for image_name in os.listdir(label_path):
                            self.image_paths.append(os.path.join(label_path, image_name))
                            self.labels.append(idx)

            def __len__(self):
                return len(self.image_paths)

            def __getitem__(self, idx):
                img_path = self.image_paths[idx]
                label = self.labels[idx]
                image = Image.open(img_path).convert('RGB')
                image = image.resize(self.image_size)
                image = np.array(image) / 255.0
                image = torch.tensor(image, dtype=torch.float32).permute(2, 0, 1)  # C, H, W
                label = torch.tensor(label, dtype=torch.long)

                return image, label

        dataset = CustomDataset(data_dir, image_size)
        dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=shuffle)
        
        return dataloader
