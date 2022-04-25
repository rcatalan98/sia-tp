import math
import random
from typing import List, Tuple, Callable

import numpy as np


class NNBuilder:
    def __init__(self):
        self.layers = []
        self.input_nodes = 0

    def with_input(n: int):
        builder = NNBuilder()
        builder.input_nodes = n
        return builder

    def with_hidden_layer(self, n: int, activation_function, derived):
        self.layers.append((n, activation_function, derived))
        return self

    def with_output_layer(self, n: int, activation_function, derived):
        self.layers.append((n, activation_function, derived))
        return self.build()

    def build(self):
        return NeuralNetwork(self.input_nodes, self.layers)


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# TODO: 1. Add bias
# TODO: 2. See if it works for 1
# TODO: 3. Generalize
class NeuralNetwork:
    def __init__(self, input_nodes: int, layers: List[Tuple[int, Callable, Callable]]):
        all_layers = [(input_nodes, None, None)] + layers

        a = [[e, e] for e in all_layers]
        b = [item for sublist in a for item in sublist]
        c = b[1:-1]
        d = chunks(c, 2)

        self.w = []

        for (prev, next) in d:
            self.w.append(np.random.uniform(-1.0, 1.0, (next[0], prev[0])))

        self.bias = []
        self.activation_functions = []
        self.derived_functions = []
        for layer in layers:
            self.bias.append(np.random.uniform(-1.0, 1.0, (layer[0], 1)))
            self.activation_functions.append(np.vectorize(layer[1]))
            self.derived_functions.append(np.vectorize(layer[2]))

        self.layer_count = len(layers)

    def feed_forward(self, data_point):
        data_point = np.array(data_point).reshape((len(data_point), 1))

        entry = data_point
        for i in range(self.layer_count):
            value = np.dot(self.w[i], entry) + self.bias[i]
            entry = self.activation_functions[i](value)

        # replace for numpy
        return entry.reshape(entry.size)

    # Este es el generico!!!!
    def train(self, data_point, result, learning_rate: float):

        data_point = np.array(data_point).reshape((len(data_point), 1))
        result = np.array(result, ndmin=2)

        # Feed forward
        excitement_values = []
        output_values = []

        entry = data_point
        for i in range(self.layer_count):
            value = np.dot(self.w[i], entry) + self.bias[i]
            excitement_values.append(value)
            output = self.activation_functions[i](value)
            output_values.append(output)
            entry = output

        final_output = output_values[-1]
        output_error = result.reshape((result.size,1)) - final_output

        # Backpropagation

        # Output layer
        errors = [output_error]
        for i in reversed(range(self.layer_count-1)):
            error = np.dot(self.w[i+1].T, errors[-1])
            errors.append(error)
        errors.reverse()

        input_for_each_layer = [data_point] + output_values
        for i in reversed(range(self.layer_count)):
            gradient = self.derived_functions[i](excitement_values[i])
            gradient = gradient * errors[i]
            gradient = gradient * learning_rate
            self.bias[i] = self.bias[i] + gradient
            delta_w = np.dot(gradient, input_for_each_layer[i].T)
            self.w[i] += delta_w

        return self.w



    # def __init__(self, input_nodes: int, hidden_nodes: int, output_nodes: int, learning_rate: float, bias: int = 1,
    #              activation_function=None, threshold: float = 0.01) -> None:
    #     self.threshold = threshold
    #     self.input_nodes = input_nodes
    #     self.output_nodes = output_nodes
    #     self.hidden_nodes = hidden_nodes
    #     self.learning_rate = learning_rate
    #     self.bias = bias
    #     self.activation_function = activation_function
    #     self.wih = np.random.uniform(-1.0, 1.0, (hidden_nodes, input_nodes + 1))
    #     self.who = np.random.uniform(-1.0, 1.0, (output_nodes, hidden_nodes + 1))

    @staticmethod
    def logistic_function(excitement_value):
        return 1 / (1 + math.exp(-4 * excitement_value))

    @staticmethod
    def g_prime(excitement):
        exp = math.exp(-4 * excitement)
        return (4 * exp) / math.pow((1 + exp), 2)

    def activation(self, excitement_value):
        return NeuralNetwork.logistic_function(excitement_value)

    def estimate_error(self, input_dataset, expected_results):
        error = 0
        for mu in range(len(input_dataset)):
            input_data = input_dataset[mu]
            expected_output = expected_results[mu]
            output = self.perform(input_data)
            error += np.sum(np.power(expected_output - output, 2))
        return error / len(input_dataset)

    # def train(self, train_dataset, expected_results):
    #
    #     for a in range(100):
    #         i = random.randint(0, len(train_dataset) - 1)
    #         # Adding the bias
    #         train_element = np.append(train_dataset[i], self.bias).reshape(self.wih.shape[1], 1)
    #
    #         assert train_element.shape == (self.wih.shape[1], 1)
    #         signals_input_hidden = np.dot(self.wih, train_element)
    #
    #         assert signals_input_hidden.shape == (self.wih.shape[0], 1)
    #         signals_hidden_output = np.array([self.activation(e) for e in signals_input_hidden], ndmin=2)
    #         # Adding the bias
    #         signals_hidden_output = np.append(signals_hidden_output, self.bias).reshape(self.who.shape[1], 1)
    #
    #         assert signals_hidden_output.shape == (self.who.shape[1], 1)
    #
    #         signals_output = np.dot(self.who, signals_hidden_output)
    #         signals_output_results = np.array([self.activation(e) for e in signals_output], ndmin=2)
    #
    #         g_prime = np.array([NeuralNetwork.g_prime(e) for e in signals_output], ndmin=2)
    #         results_diff = (expected_results[i] - signals_output_results)
    #         greek_delta_output = np.dot(g_prime, results_diff).reshape(1, 1)
    #
    #         g_prime_hidden = np.array([NeuralNetwork.g_prime(e) for e in signals_input_hidden], ndmin=2)
    #         propagated_diff = np.dot(greek_delta_output, self.who)
    #         greek_delta_hidden = np.dot(g_prime_hidden.T, propagated_diff)
    #
    #         self.who += self.learning_rate * np.dot(signals_hidden_output, greek_delta_output).T
    #         self.wih += self.learning_rate * np.dot(greek_delta_hidden, train_element)

    def perform(self, input):

        input = np.append(input, self.bias).reshape(self.wih.shape[1], 1)

        assert input.shape == (self.wih.shape[1], 1)
        signals_input_hidden = np.dot(self.wih, input)

        assert signals_input_hidden.shape == (self.wih.shape[0], 1)
        signals_hidden_output = np.array([self.activation(e) for e in signals_input_hidden], ndmin=2)
        # Adding the bias
        signals_hidden_output = np.append(signals_hidden_output, self.bias).reshape(self.who.shape[1], 1)

        assert signals_hidden_output.shape == (self.who.shape[1], 1)

        signals_output = np.dot(self.who, signals_hidden_output)
        signals_output_results = np.array([self.activation(e) for e in signals_output], ndmin=2)

        return signals_output_results
