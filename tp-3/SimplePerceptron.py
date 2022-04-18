import random

import numpy as np




class SimplePerceptron:
    def __init__(self):
        self.w = np.array()

    # Calcula la funcion w_1 *x_1 + w_2 * x_2 ...
    def excitement(self, w, datapoint):
        return np.dot(w,datapoint)

    def activation(self, excitement_value):
        return 1 if excitement_value > 0 else -1

    def estimateError(self, train_dataset, expected_results, w):
        func = np.vectorize(lambda x: self.activation(self.excitement(w,x)))
        misclassified = np.count_nonzero(func(train_dataset) == expected_results)
        return misclassified / len(expected_results)

    def train(self, train_dataset, expected_results, max_iteration, learning_rate):
        error = 1
        p = len(expected_results)
        error_min = 2 * p
        w = np.random.random(2) * 2 - 1
        self.w = np.copy(w)

        for it in range(max_iteration):
            if error == 0:
                break

            i_x = random.randint(1,p)
            h = self.excitement(w, train_dataset[i_x])
            o = self.activation(h)
            delta_w = np.dot(learning_rate * (expected_results[i_x] - o), train_dataset[i_x])
            w += delta_w
            error = self.estimateError(train_dataset,expected_results,w)

            if error < error_min:
                error_min = error
                self.w = np.copy(w)

        return self.w