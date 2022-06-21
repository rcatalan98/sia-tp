import copy
import math
import random
from typing import List, Tuple, Callable

import numpy as np
from numpy import mean
from scipy import optimize

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
        self.iterations = 0

        self.w = []
        self.shapes = []
        for (prev, next) in d:
            self.w.append(np.random.uniform(-1.0, 1.0, (next[0], prev[0])))
            self.shapes.append((next[0], prev[0]))

        self.bias = []
        self.activation_functions = []
        self.derived_functions = []
        self.prev_delta = []
        self.prev_derivative = []

        for layer in layers:
            self.bias.append(np.random.uniform(-1.0, 1.0, (layer[0], 1)))
            self.activation_functions.append(np.vectorize(layer[1]))
            self.derived_functions.append(np.vectorize(layer[2]))
            self.prev_delta.append(None)
            self.prev_derivative.append(None)

        self.layer_count = len(layers)

    def feed_forward(self, data_point, w=None, b=None, encode=True, decode=True):
        latent_space_layer = int(self.layer_count / 2)
        start = 0 if encode else latent_space_layer
        stop = self.layer_count if decode else latent_space_layer + 1

        w = self.w if w is None else w
        b = self.bias if b is None else b

        data_point = np.array(data_point).reshape((len(data_point), 1))

        entry = data_point
        entry_list = [entry]

        for i in range(start, stop):
            value = np.dot(w[i], entry)
            entry = self.activation_functions[i](value)
            entry_list.append(entry.reshape(entry.size))

        return entry_list

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

            derivative_momentum = 0.9 * (self.prev_derivative[i] if self.prev_derivative[i] is not None else 0)
            self.prev_derivative[i] = self.derived_functions[i](excitement_values[i])

            self.bias[i] += gradient + derivative_momentum

            delta_w = np.dot(gradient, input_for_each_layer[i].T)

            delta_w_momentum = 0.9 * (self.prev_delta[i] if self.prev_delta[i] is not None else 0)

            self.w[i] += delta_w + delta_w_momentum
            self.prev_delta[i] = delta_w

        return self.w, self.bias

    def iteration_callback(self, x):
        self.iterations += 1
        print(f"ITERATION {self.iterations}")

    def train_on_dataset(self, dataset, expected_results, maxiter=10):

        x0 = []
        for m in self.w:
            x0 += list(np.asarray(m).reshape(-1))

        result = optimize.minimize(self.E, x0=np.asarray(x0), method='Powell', options={'maxiter': maxiter, 'disp': True},
                                   args=(dataset, expected_results, self.layer_count, self.activation_functions),
                                   callback=self.iteration_callback
                                   )

        self.w = self.unflatten(result.x)
        errors = result.fun

        return errors, self.w

    def get_distance_on_datapoint(self, observed_result, expected_result):
        return expected_result - observed_result

    def get_error_on_dataset(self, dataset, results, w=None, b=None, threshold=0.15):
        errors = [self.error_function(self.feed_forward(dataset[i], w=w, b=b)[-1], results[i]) for i in
                  range(len(results))]
        return np.average(errors)

    def unflatten(self, w):
        w_unflatten = []
        last_pos = 0

        # unflatten w
        for i in range(len(self.shapes)):
            next = self.shapes[i][0]
            prev = self.shapes[i][1]
            w_unflatten.append(np.reshape(w[last_pos:last_pos + next * prev], self.shapes[i]))
            last_pos += next * prev
        return w_unflatten

    # Error
    def E(self, w, *args):
        input, expected_output, layer_count, activation_functions = args

        w_unflatten = self.unflatten(w)

        s = np.average(
                 sum(1/2 * (expected_output[i] - self.train_on_datapoint_with_params(
                     input[i], layer_count, w_unflatten, activation_functions) ) ** 2
                     for i in range(len(input)))
                 )
        return s

    def train_on_datapoint_with_params(self, data_point, layer_count, w, activation_functions):
        data_point = np.array(data_point).reshape((len(data_point), 1))
        entry = data_point

        for i in range(layer_count):
            value = np.dot(w[i], entry)
            output = activation_functions[i](value)
            entry = output

        return entry.reshape(entry.size)
