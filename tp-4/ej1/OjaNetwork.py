import math

import numpy as np


class OjaNetwork:
    def __init__(self, epochs: int, values, learning_rate: float = 0) -> None:
        self.epochs = epochs
        self.learning_rate = learning_rate

        mean = np.mean(values.T, axis=1)
        std = np.std(values.T, axis=1)
        values_len = len(values[0])
        self.values = (values - mean) / std

        self.w = np.random.uniform(-1, 1, values_len)

    def train(self):
        for i in range(self.epochs):
            for val in self.values:
                activation = np.dot(self.w, val)
                self.w += self.learning_rate * activation * (val - (activation * self.w))

        norm = math.sqrt(np.dot(self.w, self.w.T))
        return self.w / norm
