import numpy as np
import random

class LinearPerceptron:
    def __init__(self, dimensions):
        self.w = None
        self.dimensions = dimensions

    # Calcula la funcion w_1 *x_1 + w_2 * x_2 ...
    @staticmethod
    def excitement(w, datapoint):
        return np.dot(datapoint,w)

    def activation(self, excitement_value):
        return excitement_value

    def estimate_error(self, train_dataset, expected_results, w):
        val = np.array([self.activation(self.excitement(w, x)) for x in train_dataset]) - expected_results
        results = np.array([i**2 for i in val])
        return float(sum(results) / len(expected_results))

    def augment_dataset(self, train_dataset, value = 1):
        return np.insert(train_dataset, self.dimensions, value, axis=1)

    def delta_w(self,learning_rate, expected_result, observed_result, datapoint):
        return learning_rate * np.dot(expected_result - observed_result,datapoint)

    def train(self, train_dataset, expected_results, max_iteration, learning_rate):
        p = len(expected_results)
        error = 1
        error_min = 2 * p
        train_dataset = self.augment_dataset(train_dataset)
        w = np.ones(self.dimensions + 1)
        self.w = np.copy(w)
        it = 0
        while error > 0.1 and it < max_iteration:
            i_x = random.randint(0, p - 1)
            h = self.excitement(w,train_dataset[i_x])
            o = self.activation(h)
            delta_w = self.delta_w(learning_rate,expected_results[i_x],o,train_dataset[i_x])
            w = np.add(w,delta_w)
            error = self.estimate_error(train_dataset, expected_results, w)
            if error < error_min:
                error_min = error
                self.w = np.copy(w)
            # else:
            #      w = np.copy(self.w)

            it += 1
            print(f'Iteration number:{it}, error: {error}, w: {w}')



        return self.w

    def perform(self,value):
        return self.activation(self.excitement(self.w,self.augment_dataset(np.array([value]))))