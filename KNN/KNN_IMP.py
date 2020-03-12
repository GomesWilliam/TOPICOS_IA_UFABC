from scipy.stats import mode

class KNN_Classifier:
    xTrain = []
    yTrain = []
    yTest = []
    k_smaller = []
    k = 0
    
    def __init__(self, k = 5):
        self.k = k
        
    def fit(self, xTrain, yTrain):
        self.xTrain = xTrain
        self.yTrain = yTrain
    
    def predict(self, xTest):
        dists_result = []
        dists_result = self._dist_calculation_all(self.xTrain, xTest, self.yTrain)
        self.insertion_sort_all(dists_result)
        self.k_smaller = self._get_k_neighborhood_all(dists_result, self.k)
        self.k_smaller =self._get_mode(self.k_smaller)
        return self.k_smaller
        
        
    def _euclidian_dist(self, arrayA, arrayB):
        dist = 0
        for i, j in zip(arrayA, arrayB):
            dist += (i - j)**2
        return dist**(1/2)

    def _dist_calculation(self, xTrain, xTest, yTrain):
        i = 0
        dist_target = []
        for instances in self.xTrain:
            dist = self._euclidian_dist(instances, xTest)
            dist_target.append([dist, yTrain[i]])
            i += 1    
        return dist_target

    def _dist_calculation_all(self, xTrain, xTest, yTrain,):
        dists_all = []
        for index in range(0, len(xTest)):
            dists_all.append(self._dist_calculation(xTrain, xTest[index], yTrain))
        return dists_all

#     def insertion_sort(self, array):
#         for index in range(1, len(array)):
#             currentValue = array[index]
#             currentPosition = index

#         while currentPosition > 0 and array[currentPosition - 1] > currentValue:
#             array[currentPosition] = array[currentPosition -1]
#             currentPosition = currentPosition - 1

#         array[currentPosition] = currentValue
#   
        
    def insertion_sort_all(self, array):
#         for array_each_sample in array:
#             for index in range(1, len(array_each_sample)):
#                 currentValue = array_each_sample[index]
#                 currentPosition = index

#             while currentPosition > 0 and array_each_sample[currentPosition - 1] > currentValue:
#                 array_each_sample[currentPosition] = array_each_sample[currentPosition -1]
#                 currentPosition = currentPosition - 1

#             array_each_sample[currentPosition] = currentValue
        
        
        for distanciasParaDadoTesteAtual in array:
            
            # EU A ORDENO
            for i in range(len(distanciasParaDadoTesteAtual) - 1):
                for j in range(i+1, len(distanciasParaDadoTesteAtual)):
                    
                    if distanciasParaDadoTesteAtual[j] < distanciasParaDadoTesteAtual[i]:
                        linhaAux = distanciasParaDadoTesteAtual[j]
                        distanciasParaDadoTesteAtual[j] = distanciasParaDadoTesteAtual[i]
                        distanciasParaDadoTesteAtual[i] = linhaAux

#         for i in range(0, len(array)):
#             array[i].sort()
    

    def _get_k_neighborhood(self, array, k):
        k_smaller = []
        k_smaller = array[:k]
        k_smaller_class = []
        for index in range(0, k):
            k_smaller_class.append(k_smaller[index][1])
        return k_smaller_class
    
    def _get_k_neighborhood_all(self, array, k):
        k_smaller_all = []
        for index in range(0, len(array)):
            k_smaller_all.append(self._get_k_neighborhood(array[index], k))
        return k_smaller_all
      
    def _get_mode(self, array):
        mode_array = []
        for index in range(0, len(array)):
            moda = mode(array[index])[0][0]
            mode_array.append(moda)
        return mode_array