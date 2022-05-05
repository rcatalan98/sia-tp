import math
import random

import numpy as np

from NeuralNetwork import NNBuilder
from Utils import shuffle_data, normalize_array


def LinearPerceptron(iterations=500, epochs=100, learning_rate=0.0001):
    with open("train_dataset.txt", 'r') as file:
        input = [[float(a) for a in i.split(',')] for i in file.readlines()]

    with open("expected_output.txt", 'r') as file:
        results = [float(i) for i in file.readlines()]

    input, results = shuffle_data(input, results)
    training_data_input = input[180:]
    training_data_output = results[180:]
    test_data_input = input[:180]
    test_data_output = results[:180]

    nn = NNBuilder.with_input(3).with_output_layer(1, lambda x: x, lambda x: 1)

    (training_errors,ws,bs) = nn.train_on_dataset(training_data_input, training_data_output, iterations, epochs, learning_rate)

    # for i in range(len(test_data_output)):
    #     print(f"expected; {test_data_output[i]}, got: {nn.feed_forward(test_data_input[i])}")

    test_error = nn.get_error_on_dataset(test_data_input, test_data_output)
    print(f"Test error:{test_error}")

    # TODO: analyse possible refactor
    # testing_errors_sum = 0
    # for i in range(len(test_data_output)):
    #     nn_output = nn.feed_forward(test_data_input[i])
    #     print(f"expected; {test_data_output[i]}, got: {nn_output}")
    #     testing_errors_sum += (nn_output - test_data_output[i]) ** 2 / 2
    #
    # testing_error = testing_errors_sum / len(test_data_output)
    # print(f"Test error:{testing_error}")


sigmoid = lambda e: 1 / (1 + math.exp(-e))
sigmoid_derived = lambda e: sigmoid(e) * (1 - sigmoid(e))


def NotLinearPerceptron(iterations=100, epochs=5000, learning_rate=0.01):
    with open("train_dataset.txt", 'r') as file:
        input = [[float(a) for a in i.split(',')] for i in file.readlines()]

    with open("expected_output.txt", 'r') as file:
        results = normalize_array([float(i) for i in file.readlines()])

    input, results = shuffle_data(input, results)
    training_data_input = input[:180]
    training_data_output = results[:180]
    test_data_input = input[180:]
    test_data_output = results[180:]

    nn = NNBuilder.with_input(3).with_output_layer(1, sigmoid, sigmoid_derived)

    (training_errors,ws) = nn.train_on_dataset(training_data_input, training_data_output, iterations, epochs, learning_rate)

    for i in range(len(test_data_output)):
        print(f"expected; {test_data_output[i] * 100}, got: {nn.feed_forward(test_data_input[i]) * 100}")

    test_error = nn.get_error_on_dataset(test_data_input, test_data_output)
    print(f"Test error:{test_error}")

    # TODO: analyse possible refactor
    # testing_errors_sum = 0
    # for i in range(len(test_data_output)):
    #     nn_output = nn.feed_forward(test_data_input[i])
    #     print(f"expected; {test_data_output[i] * 100}, got: {nn_output * 100}")
    #     testing_errors_sum += (nn_output - test_data_output[i])**2/2
    #
    # testing_error = testing_errors_sum / len(test_data_output)
    # print(f"Test error:{testing_error}")
