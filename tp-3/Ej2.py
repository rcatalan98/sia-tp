import math
import random

import numpy as np

from NeuralNetwork import NNBuilder




def LinearPerceptron():
    with open("train_dataset.txt", 'r') as file:
        input = [[float(a) for a in i.split(',')] for i in file.readlines()]

    with open("expected_output.txt", 'r') as file:
        results = [float(i) for i in file.readlines()]

    min = np.min(results)
    max = np.max(results)

    normalized_results = [(res - min) / (max - min) for res in results]

    data = [ (input[i],normalized_results[i]) for i in range(len(results))]

    np.random.shuffle(data)
    training_data = data[180:]
    test_data = data[:180]

    nn = NNBuilder.with_input(3).with_output_layer(1, lambda x: x, lambda x: 1)

    for _ in range(50000):
        (data_point, result) = training_data[random.randint(0,len(training_data)-1)]
        nn.train(data_point, result, 0.01)

    for (data_point, result) in test_data:
        print(f"expected; {result}, got: {nn.feed_forward(data_point)}")


sigmoid = lambda e: 1 / (1 + math.exp(-e))
sigmoid_derived = lambda e: sigmoid(e) * (1 - sigmoid(e))

def NotLinearPerceptron():
    with open("train_dataset.txt", 'r') as file:
        input = [[float(a) for a in i.split(',')] for i in file.readlines()]

    with open("expected_output.txt", 'r') as file:
        results = [float(i) for i in file.readlines()]

    min = np.min(results)
    max = np.max(results)

    normalized_results = [(res - min) / (max - min) for res in results]

    data = [ (input[i],normalized_results[i]) for i in range(len(results))]

    np.random.shuffle(data)
    training_data = data[180:]
    test_data = data[:180]

    nn = NNBuilder.with_input(3).with_output_layer(1, sigmoid, sigmoid_derived)

    for _ in range(50000):
        (data_point, result) = training_data[random.randint(0,len(training_data)-1)]
        nn.train(data_point, result, 0.01)

    for (data_point, result) in test_data:
        print(f"expected; {result}, got: {nn.feed_forward(data_point)}")
