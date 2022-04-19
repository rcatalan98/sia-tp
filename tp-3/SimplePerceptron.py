import random

import numpy as np


class SimplePerceptron:
    def __init__(self):
        self.w = None

    # Calcula la funcion w_1 *x_1 + w_2 * x_2 ...
    @staticmethod
    def excitement(w, datapoint):
        return np.dot(datapoint,w) #esto no calcula lo que queremos!

    @staticmethod
    def activation(excitement_value):
        return 1 if excitement_value >= 0 else -1

    def estimate_error(self, train_dataset, expected_results, w):
        results = np.array([self.activation(self.excitement(w, x)) for x in train_dataset])
        misclassified = np.count_nonzero(results != expected_results)
        return float(misclassified / len(expected_results))

    def augment_dataset(self, train_dataset, position=2 ,value = 1):
        return np.insert(train_dataset, position, value, axis=1)

    def train(self, train_dataset, expected_results, max_iteration, learning_rate):
        p = len(expected_results)
        error = 1
        error_min = 2 * p
        train_dataset = self.augment_dataset(train_dataset)
        w = np.zeros(3)
        self.w = np.copy(w)
        it = 0
        while error > 0 and it < max_iteration:
            # print(f'Iteration number:{it}, error: {error}, w: {w}')
            i_x = random.randint(0, p - 1)
            h = self.excitement(w,train_dataset[i_x])
            o = self.activation(h)
            delta_w = learning_rate * np.dot(expected_results[i_x] - o, train_dataset[i_x])
            w = np.add(w,delta_w)
            error = self.estimate_error(train_dataset, expected_results, w)
            if error < error_min:
                error_min = error
                self.w = np.copy(w)
            else:
                w = np.copy(self.w)

            it += 1

        print(f'Iteration number:{it}, error: {error}, w: {w}')

        return self.w

    def perform(self,value):
        return self.activation(self.excitement(self.w,self.augment_dataset(np.array([value]))))