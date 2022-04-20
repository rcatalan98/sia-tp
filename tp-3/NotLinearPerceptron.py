import math
import mpmath

from LinearPerceptron import LinearPerceptron


class NotLinearPerceptron(LinearPerceptron):
    def __init__(self, dimensions, beta, threshold=1):
        super().__init__(dimensions,threshold)
        self.beta = beta

    def activation(self, excitement_value):
        return math.tanh(self.beta * excitement_value)

    def delta_w(self,learning_rate, expected, observed, datapoint):
        return super().delta_w(learning_rate, expected, observed, datapoint) \
               * self.beta * float(mpmath.sech(self.beta * observed)**2)




