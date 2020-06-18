import numpy as np

class LMS:

    def __init__(self):
        self.weights = None
        self.bias = None
        self.bias_weights = None
        self.Xn = None
        
    def fit(self, X, y):
        try:
            samples, features = X.shape
        except:
            features = 1
            samples = X.size
        
        X = X.reshape(-1,1)
        self.bias = np.ones((samples, 1))
        self.Xn = np.append(X, self.bias, axis = 1)
        
        self.weights = np.matmul(np.matmul(np.linalg.inv(np.matmul(self.Xn.T, self.Xn)), self.Xn.T), y.T)

    def predict(self, X):
        output = np.dot(X, self.weights[0]) + self.weights[1] 
        y_predict = output
        return y_predict
