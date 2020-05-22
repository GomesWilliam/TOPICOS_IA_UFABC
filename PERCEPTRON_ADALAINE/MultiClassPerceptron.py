import numpy as np
class MCPerceptron:
    pesos = []
    pesos_bias = []
    def __init__(self, learning_rate = 0.1, epochs = 100):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.bias_weights = None
        self.n_class = None
        self.unique_classes = None
        self.acuracias = []
        self.pesos = []
        self.pesos_bias = []

    def _act_func(self, y):
        #does nor work for array
        #return 1 if y >= 0 else 0
        return np.where(y>=0, 1, 0)

    def fit(self, X, y):
#        print('Iniciando Treinamento')
        self.unique_classes = self._unique(y)
        self.n_class = len(self.unique_classes)
        
        for claS in self.unique_classes:
#            print('Iniciando classe:')
#            print(claS)
            classes = np.array([1 if x == claS else 0 for x in y])
#            print('Valore das classes transformadas: ', classes)
            self._training(X, classes)




    def _training(self, X, y):
                self.samples, features = X.shape
                self.weights = 0.10 * np.random.randn(features)
                self.bias_weights = 0.10 * np.random.randn(1)
                self.bias = -1.

                for j in range(self.epochs):
                    predict_right = 0
                    predict_wrong = 0

                    for i, x in enumerate(X):
                        predict = 0
                        output = np.dot(x, self.weights) +  self.bias_weights * self.bias
                        y_predict = self._act_func(output)
                        erro = y[i] - y_predict
                        if(erro == 0):
                            predict_right+= 1
                        else:
                            predict_wrong+= 1
                        update = self.learning_rate * erro
                        self.weights +=  update * x
                        self.bias_weights += update * self.bias

                    weights_copy = np.copy(self.weights)
                    weights_bias_copy = np.copy(self.bias_weights)

                    self.pesos.append(weights_copy)
                    self.pesos_bias.append(weights_bias_copy)
                    self.acuracias.append((predict_right)/(predict_right + predict_wrong))

    def _unique(self, list1):
        x = np.array(list1)
        return np.unique(x)

    def predict(self, X):
        y_predict_list = []
        for n, claS in enumerate(self.unique_classes):
            output = np.dot(X, self.pesos[(self.epochs*(n+1) -1)]) +  self.pesos_bias[(self.epochs*(n+1) -1)] * self.bias
            y_predict = output
            y_predict_list.append(y_predict)
          
        y_predict_final = []
        for i in range(len(y_predict_list[0])):
            y_predict_final.append(0)
        higher = y_predict_list[0]
#        print(y_predict_list)
        for n, claS in enumerate(self.unique_classes):
            for i, value in enumerate(y_predict_list[n]):
#               print(value)
                if(value >= higher[i]):
#                    print('ENTROU AQUI')
                    y_predict_final[i] = claS;
                    higher[i] = value;
                    
        return y_predict_final

    #def predict(self, X):
        #output = np.dot(X, self.weights) + self.bias_weights * self.bias
        #y_predict = self._act_func(output)
        #return y_predict
    
    