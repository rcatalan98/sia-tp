import math
import random

import numpy as np

from NeuralNetwork import NNBuilder
from Utils import shuffle_data, normalize_array

beta = 0.5
sigmoid = lambda e: 1 / (1 + math.exp(-e * 2 * beta))
sigmoid_derived = lambda e: 2 * beta * sigmoid(e) * (1 - sigmoid(e))

def LinearPerceptron(iterations=500, epochs=100, learning_rate=0.0001, training_ratio= 0.8):

    with open("train_dataset.txt", 'r') as file:
        input = [[float(a) for a in i.split(',')] for i in file.readlines()]

    with open("expected_output.txt", 'r') as file:
        results = [float(i) for i in file.readlines()]
    limit = math.floor(len(input) * training_ratio)
    input, results = shuffle_data(input, results)
    training_data_input = input[:limit]
    training_data_output = results[:limit]
    test_data_input = input[limit:]
    test_data_output = results[limit:]

    nn = NNBuilder.with_input(3).with_output_layer(1, lambda x: x, lambda x: 1)

    (training_errors,ws,bs) = nn.train_on_dataset(training_data_input, training_data_output, epoch_size=iterations, epochs=epochs, learning_rate=learning_rate)

    # for i in range(len(test_data_output)):
    #     print(f"expected; {test_data_output[i]}, got: {nn.feed_forward(test_data_input[i])}")

    # test_error = nn.get_error_on_dataset(test_data_input, test_data_output)
    # print(f"Test error:{test_error}")

    results = dict()
    results['training_error'] = training_errors
    results['testing_error'] = [nn.get_error_on_dataset(test_data_input, test_data_output,ws[i],bs[i]) for i in
                                range(len(ws))]
    return results




def NotLinearPerceptron(iterations=100, epochs=5000, learning_rate=0.01, b=beta, training_ratio= 0.8):
    with open("train_dataset.txt", 'r') as file:
        input = [[float(a) for a in i.split(',')] for i in file.readlines()]

    with open("expected_output.txt", 'r') as file:
        results = normalize_array([float(i) for i in file.readlines()])

    list_of_globals = globals()
    list_of_globals['beta'] = b
    limit = math.floor(len(input) * training_ratio)
    input, results = shuffle_data(input, results)
    training_data_input = input[:limit]
    training_data_output = results[:limit]
    test_data_input = input[limit:]
    test_data_output = results[limit:]

    nn = NNBuilder.with_input(3).with_output_layer(1, sigmoid, sigmoid_derived)

    (training_errors, ws, bs) = nn.train_on_dataset(training_data_input, training_data_output, epoch_size=iterations, epochs=epochs, learning_rate=learning_rate)


    results = dict()
    results['training_error'] = training_errors
    results['testing_error'] = [nn.get_error_on_dataset(test_data_input, test_data_output, ws[i], bs[i]) for i in
                                range(len(ws))]
    return results