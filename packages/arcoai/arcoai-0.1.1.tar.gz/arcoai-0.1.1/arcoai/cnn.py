import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization

class CNN:
    def __init__(self, input_shape, conv_layers, dense_layers, activation="relu", output_activation="softmax"):
        self.model = Sequential()
        
        for i, (filters, kernel_size, pool_size) in enumerate(conv_layers):
            if i == 0:
                self.model.add(Conv2D(filters, kernel_size, activation=activation, input_shape=input_shape))
            else:
                self.model.add(Conv2D(filters, kernel_size, activation=activation))
            self.model.add(BatchNormalization())
            self.model.add(MaxPooling2D(pool_size=pool_size))
            self.model.add(Dropout(0.25))
        
        self.model.add(Flatten())

        for units in dense_layers[:-1]:
            self.model.add(Dense(units, activation=activation))
            self.model.add(Dropout(0.5))

        self.model.add(Dense(dense_layers[-1], activation=output_activation))

    def compile(self, optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]):
        self.model.compile(optimizer=optimizer, loss=loss, metrics=metrics)

    def train(self, X_train, y_train, X_val=None, y_val=None, epochs=20, batch_size=32):
        if X_val is not None and y_val is not None:
            return self.model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=batch_size)
        return self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def evaluate(self, X_test, y_test):
        return self.model.evaluate(X_test, y_test)

    def predict(self, X):
        return self.model.predict(X)

    def summary(self):
        self.model.summary()
