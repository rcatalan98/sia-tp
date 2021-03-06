import copy
import math
import random
from typing import List, Tuple, Callable

import numpy as np

from Utils import chunks, flatten_array


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

    def with_output_layer(self, n: int, activation_function, derived, error_function=None):
        self.layers.append((n, activation_function, derived))
        self.error_function = error_function
        return self.build()

    def build(self):
        return NeuralNetwork(self.input_nodes, self.layers, self.error_function)


class NeuralNetwork:
    def __init__(self, input_nodes: int, layers: List[Tuple[int, Callable, Callable]], error_function: Callable = None):
        all_layers = [(input_nodes, None, None)] + layers

        self.error_function = (lambda a, b: 0.5 * (a - b) ** 2) if error_function is None else error_function

        a = [[e, e] for e in all_layers]
        b = flatten_array(a)
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

    def feed_forward(self, data_point, w=None, b=None):
        w = self.w if w is None else w
        b = self.bias if b is None else b

        data_point = np.array(data_point).reshape((len(data_point), 1))

        entry = data_point
        for i in range(self.layer_count):
            value = np.dot(w[i], entry) + b[i]
            entry = self.activation_functions[i](value)

        return entry.reshape(entry.size)

    def train_on_datapoint(self, data_point, result, learning_rate: float):
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
        output_error = self.get_distance_on_datapoint(final_output, result.reshape((result.size, 1)))

        # Backpropagation
        errors = [output_error]
        for i in reversed(range(self.layer_count - 1)):
            error = np.dot(self.w[i + 1].T, errors[-1])
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

        return self.w, self.bias

    def train_on_dataset(self, dataset, expected_results, epochs, epoch_size, learning_rate):
        errors = []
        best_w = None
        min_error = float("inf")
        w = []
        b = []
        ws = []
        bs = []
        for _ in range(epochs):
            for _ in range(epoch_size):
                i = random.randint(0, len(expected_results) - 1)
                (w, b) = self.train_on_datapoint(dataset[i], expected_results[i], learning_rate)
            errors.append(self.get_error_on_dataset(dataset, expected_results))
            ws.append(copy.deepcopy(w))
            bs.append(copy.deepcopy(b))

            if errors[-1] < min_error:
                min_error = errors[-1]
                best_w = copy.deepcopy(w)

        self.w = best_w
        return errors, ws, bs

    def get_distance_on_datapoint(self, observed_result, expected_result):
        return expected_result - observed_result

    def get_error_on_dataset(self, dataset, results, w=None, b=None, threshold=0.15):
        errors = [self.error_function(self.feed_forward(dataset[i], w=w, b=b), results[i]) for i in
                  range(len(results))]
        return np.average(errors)
