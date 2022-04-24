import math

import numpy as np


class NeuralNetwork:
    def __init__(self, input_nodes: int, hidden_nodes: int, output_nodes: int, learning_rate: float, bias: int,
                 activation_function=None, threshold: float = 0.01) -> None:
        self.threshold = threshold
        self.input_nodes = input_nodes
        self.output_nodes = output_nodes
        self.hidden_nodes = hidden_nodes
        self.learning_rate = learning_rate
        self.bias = bias
        self.activation_function = activation_function
        self.wih = np.random.uniform(-1.0, 1.0, (input_nodes, hidden_nodes))
        self.who = np.random.uniform(-1.0, 1.0, (hidden_nodes, output_nodes))

    @staticmethod
    def logistic_function(excitement_value):
        return 1 / (1 + math.exp(-4 * excitement_value))

    @staticmethod
    def g_prime(excitement):
        exp = math.exp(-4 * excitement)
        return (4 * exp) / math.pow((1 + exp), 2)

    def activation(self, excitement_value):
        return NeuralNetwork.logistic_function(excitement_value)

    def estimate_error(self, signals_output_results, expected_results):
        return 0.5 * np.sum(np.power(expected_results - signals_output_results, 2))

    def train(self, train_dataset, expected_results, max_iteration):

        for i in range(len(train_dataset)):

            train_element = train_dataset[i]
            signals_input_hidden = np.dot(self.wih, train_element)
            signals_hidden_output = np.array([self.activation(e) for e in signals_input_hidden])

            signals_output = np.dot(signals_hidden_output, self.who)
            signals_output_results = np.array([self.activation(e) for e in signals_output])

            greek_delta_output = np.dot(np.array([NeuralNetwork.g_prime(e) for e in signals_output]),
                                        expected_results[i] - signals_output_results)

            greek_delta_hidden = np.dot(np.array([[NeuralNetwork.g_prime(e) for e in signals_input_hidden]]).T,
                                        np.dot(self.who, greek_delta_output).T)

            self.who += np.array([self.learning_rate * np.dot(greek_delta_output, signals_hidden_output)]).T
            self.wih += np.array([self.learning_rate * np.dot(greek_delta_hidden, train_element)]).T

            error = self.estimate_error(signals_output_results, expected_results[i])

            if error < self.threshold:
                return
