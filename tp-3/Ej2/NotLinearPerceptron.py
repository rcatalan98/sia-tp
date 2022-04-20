import math
import mpmath

from Ej2.LinearPerceptron import LinearPerceptron


class NotLinearPerceptron(LinearPerceptron):
    def __init__(self, dimensions,beta):
        super().__init__(dimensions)
        self.beta = beta

    def activation(self, excitement_value):
        return math.tanh(self.beta * excitement_value)

    def delta_w(self, learning_rate, expected_result, observed_result, datapoint):
        return super().delta_w(learning_rate, expected_result, observed_result, datapoint) * self.beta * float(mpmath.sech(self.beta * observed_result))




