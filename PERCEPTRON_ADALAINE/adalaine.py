import numpy as np
class Adalaine:
    def __init__(self, learning_rate = 0.1, epochs = 100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.bias_weights = None
        self.mse_errors_epoch = []
        
    def fit(self, X, y):
        try:
            samples, features = X.shape
        except:
            features = 1
            samples = X.size

            
        self.weights = 0.10 * np.random.randn(features)
        self.bias_weights = 0.10 * np.random.randn(1)
        self.bias = 1.
        
        for _ in range(self.epochs):
            errors = []
            for i, x in enumerate(X):
                y_predict = np.dot(x, self.weights) +  self.bias_weights * self.bias
                erro = (y[i] - y_predict)
                errors.append(erro*erro)
                update = self.learning_rate * erro
                self.weights +=  update * x
                self.bias_weights += update * self.bias
            self.mse_errors_epoch.append(np.mean(errors))
            
    def predict(self, X):
        output = np.dot(X, self.weights[0]) + self.bias_weights * self.bias
        y_predict = output
        return y_predict
