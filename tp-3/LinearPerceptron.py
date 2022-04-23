import numpy as np
import random

from SimplePerceptron import SimplePerceptron


class LinearPerceptron(SimplePerceptron):
    def __init__(self, dimensions, threshold=1):
        super().__init__(dimensions, threshold)

    def activation(self, excitement_value):
        return excitement_value

    def estimate_error(self, train_dataset, expected_results, w):
        error = 0.0
        for j in range(len(expected_results)):
            error += (self.activation(self.excitement(w,train_dataset[j])) - expected_results[j])**2
        return error / float(len(expected_results))

    def train(self, train_dataset, expected_results, max_iteration, learning_rate):
        error = 1
        error_min = float("inf")
        p = len(expected_results)
        train_dataset = self.augment_dataset(train_dataset)
        w = np.zeros(self.dimensions + 1)
        self.w = np.copy(w)
        it = 0
        while error > 0.0001 and it < max_iteration:
            for mu in range(p):
                # if it < 50:
                #     w = np.zeros_like(w) # np.random.random(self.dimensions + 1) * 2 -1

                for i in range(self.dimensions+1):
                    w[i] += self.delta_w_i(expected_results, i, learning_rate, mu, train_dataset, w)

                error = self.estimate_error(train_dataset, expected_results, w)

                if error < error_min:
                    error_min = error
                    self.w = np.copy(w)
                else:
                    w = np.copy(self.w)

            it += 1
            # print(f'Iteration number:{it}, error: {error}, w: {w}')

        print(f'Iteration number:{it}, error: {error}, w: {w}')

        return self.w

    def delta_w_i(self, expected_results, i, learning_rate, mu, train_dataset, w):
        return learning_rate * (expected_results[mu] - self.activation(self.excitement(w, train_dataset[mu]))) * \
               train_dataset[mu][i]

