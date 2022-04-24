import random

import numpy as np

# Todo remove weight from biases.
class SimplePerceptron:
    def __init__(self, dimensions, threshold = 1):
        self.w = None
        self.dimensions = dimensions

        self.threshold = threshold

    # Calcula la funcion w_1 *x_1 + w_2 * x_2 ...
    def excitement(self,w, datapoint):
        value = 0
        for i in range(self.dimensions + 1):
            value += w[i] * datapoint[i]

        return value
        # return np.dot(datapoint,w)

    def activation(self, excitement_value):
        return 1 if excitement_value >= 0 else -1

    def estimate_error(self, train_dataset, expected_results, w):
        results = np.array([self.activation(self.excitement(w, x)) for x in train_dataset])
        misclassified = np.count_nonzero(results != expected_results)
        return float(misclassified / len(expected_results))

    def augment_dataset(self, train_dataset):
        return np.insert(train_dataset,0, self.threshold, axis=1)

    # TODO: Deberia devolver un vector esto
    def delta_w(self,learning_rate, expected, observed, datapoint):
        return learning_rate * np.dot(expected - observed, datapoint)

    def train(self, train_dataset, expected_results, max_iteration, learning_rate):
        p = len(expected_results)
        error = 1
        error_min = float("inf")
        train_dataset = self.augment_dataset(train_dataset)
        w = np.zeros(self.dimensions + 1)
        self.w = np.copy(w)
        it = 0
        while error > 0 and it < max_iteration:
            i_x = random.randint(0, p - 1)
            h = self.excitement(w,train_dataset[i_x])
            o = self.activation(h)
            delta_w = self.delta_w(learning_rate,expected_results[i_x],o,train_dataset[i_x])
            w = np.add(w,delta_w)
            error = self.estimate_error(train_dataset, expected_results, w)
            if error < error_min:
                error_min = error
                self.w = np.copy(w)
            else:
                w = np.copy(self.w)

            it += 1
            print(f'Iteration number:{it}, error: {error}, w: {w}')

        print(f'Iteration number:{it}, error: {error}, w: {w}')

        return self.w

    def perform(self,value):
        return self.activation(self.excitement(self.w,self.augment_dataset(np.array([value]))[0]))