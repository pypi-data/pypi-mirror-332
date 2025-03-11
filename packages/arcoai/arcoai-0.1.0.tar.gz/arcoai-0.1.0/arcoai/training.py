class Trainer:
    def __init__(self, model, optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]):
        self.model = model
        self.optimizer = optimizer
        self.loss = loss
        self.metrics = metrics

    def compile(self):
        self.model.compile(optimizer=self.optimizer, loss=self.loss, metrics=self.metrics)

    def train(self, X_train, y_train, X_val=None, y_val=None, epochs=20, batch_size=32):
        if X_val is not None and y_val is not None:
            return self.model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=epochs, batch_size=batch_size)
        return self.model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size)

    def evaluate(self, X_test, y_test):
        return self.model.evaluate(X_test, y_test)

    def predict(self, X):
        return self.model.predict(X)
