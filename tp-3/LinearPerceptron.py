import numpy as np
import random

from SimplePerceptron import SimplePerceptron


class LinearPerceptron(SimplePerceptron):
    def __init__(self, dimensions, threshold=1):
        super().__init__(dimensions, threshold)

    def activation(self, excitement_value):
        return excitement_value

    def estimate_error(self, train_dataset, expected_results, w):
        val = np.array([self.activation(self.excitement(w, x)) for x in train_dataset]) - expected_results
        results = np.array([i**2 for i in val])
        return float(sum(results) / len(expected_results))
