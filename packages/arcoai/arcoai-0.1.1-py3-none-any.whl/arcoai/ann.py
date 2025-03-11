import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, BatchNormalization

class ANN:
    def __init__(self, input_shape, layers, activation="relu", output_activation="softmax"):
        self.model = Sequential()
        self.model.add(Dense(layers[0], activation=activation, input_shape=(input_shape,)))
        
        for units in layers[1:]:
            self.model.add(Dense(units, activation=activation))
            self.model.add(BatchNormalization())
            self.model.add(Dropout(0.2))

        self.model.add(Dense(layers[-1], activation=output_activation))

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
