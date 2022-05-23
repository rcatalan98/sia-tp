import math
import random

import numpy as np


class KohonenNetwork:
    def __init__(self, n: int, values, weightEntries: bool = False):
        mean = np.mean(values.T, axis=1)
        std = np.std(values.T, axis=1)
        self.values = (values - mean) / std
        input_length = len(values[0])
        self.w = np.empty((n, n, input_length))
        self.n = n
        for i in range(n):
            for j in range(n):
                self.w[i, j] = self.values[random.randint(0, len(values) - 1)] if weightEntries \
                    else np.random.uniform(0, 0, input_length)

    def train(self, epochs: int):
        for t in range(1, epochs):
            learning_rate = 1 / t
            radius = max(1, self.n - (2 / epochs) * t * self.n)
            for value in self.values:
                i, j = self.classify(value)
                self.update(value, i, j, radius, learning_rate)

    # Esta funcion devuelve la neurona que tiene la menor distancia normalizada al valor de entrada
    def classify(self, value):
        chosen_i, chosen_j = 0, 0
        d_min = float("inf")

        for i in range(self.n):
            for j in range(self.n):
                d = np.linalg.norm(self.w[i, j] - value)
                if d < d_min:
                    d_min = d
                    chosen_i, chosen_j = i, j

        return chosen_i, chosen_j

    def update(self, value, i, j, radius, learning_rate):
        x_neighboring_neurons = range(max(0, math.floor(i - radius)), 1 + min(self.n - 1, math.ceil(i + radius)))
        y_neighboring_neurons = range(max(0, math.floor(j - radius)), 1 + min(self.n - 1, math.ceil(j + radius)))

        for x in x_neighboring_neurons:
            for y in y_neighboring_neurons:
                if np.linalg.norm(np.subtract((x, y), (i, j))) < radius:
                    self.w[x, y] += learning_rate * (value - self.w[x, y])

    def distance_matrix(self):
        distance = np.empty((self.n, self.n))
        for i, j in np.ndindex(distance.shape):
            distance[i,j] = np.average([np.linalg.norm(self.w[i, j] - n) for n in self.neighboring_neurons(i,j)])
        return distance

    def neighboring_neurons(self,i,j,radius = 1):
        x_neighboring_neurons = range(max(0, math.floor(i - radius)), 1 + min(self.n - 1, math.ceil(i + radius)))
        y_neighboring_neurons = range(max(0, math.floor(j - radius)), 1 + min(self.n - 1, math.ceil(j + radius)))

        neurons = []
        for x in x_neighboring_neurons:
            for y in y_neighboring_neurons:
                neurons.append(self.w[x,y])

        return neurons






















