import math
# Todo remove weight from biases.
from LinearPerceptron import LinearPerceptron


class NotLinearPerceptron(LinearPerceptron):
    def __init__(self, dimensions, beta, threshold=1):
        super().__init__(dimensions,threshold)
        self.beta = beta

    def activation(self, excitement_value):
        return 1 / (1 + math.exp(-self.beta * excitement_value))
        # return math.tanh(self.beta * excitement_value)



    def g_prime(self, excitement):
        exp = math.exp(-self.beta * excitement)
        return (self.beta * exp) / math.pow((1+exp),2)

    def delta_w_i(self, expected_results, i, learning_rate, mu, train_dataset, w):
        return super().delta_w_i(expected_results, i, learning_rate, mu, train_dataset, w) * \
               self.g_prime(self.excitement(w, train_dataset[mu]))
        # self.beta * (1 - math.tanh(self.excitement(w, train_dataset[mu]))**2)
#







