import math
import random
import numpy as np

from NeuralNetwork import NNBuilder
from Utils import flatten_array, shuffle_data, avg

sigmoid = lambda e: 1 / (1 + math.exp(-e))
sigmoid_derived = lambda e: sigmoid(e) * (1 - sigmoid(e))


def MultilayerPerceptronXor(hidden_layer_nodes: int = 5, iterations=600, epochs=75, learning_rate=0.7):
    nn = NNBuilder\
                    .with_input(2)\
                    .with_hidden_layer(hidden_layer_nodes, sigmoid, sigmoid_derived)\
                    .with_output_layer(1, sigmoid, sigmoid_derived)

    xor_data_set = [[0, 1], [1, 0], [0, 0], [1, 1]]
    xor_expected_results = [1, 1, 0, 0]

    errors = nn.train_on_dataset(xor_data_set, xor_expected_results, iterations, epochs, learning_rate)

    print(errors[-1])
    for val in xor_data_set:
        print(f"\t{val[0]} \txor \t{val[1]} \tis \t{round(nn.feed_forward(val)[0])}")

    return errors[-1], nn.get_error_on_dataset(xor_data_set, xor_expected_results)


def MultilayerPerceptronMnistEvenOrOdd(hidden_layer_nodes: int = 30, iterations=100, epochs=30, learning_rate=0.1):
    nn = NNBuilder \
        .with_input(7*5) \
        .with_hidden_layer(hidden_layer_nodes, sigmoid, sigmoid_derived) \
        .with_output_layer(2, sigmoid, sigmoid_derived)

    with open("numbers.txt", 'r') as file:
        input = np.array(flatten_array([[float(a) for a in i.replace("\n","").split(' ')] for i in file.readlines()]))

        digits_input = input.reshape((10, 7*5))

        dataset = []
        results = []

        for i in range(10):
            digit = digits_input[i]
            dataset.append(digit)
            expected = [(i + 1) % 2, i % 2]
            results.append(expected)

        dataset, result = shuffle_data(dataset, results)  # FIXME: pisar results? (falto la s?)

        training_input = dataset[:9]
        training_output = result[:9]
        test_input = dataset[9:]
        test_output = result[9:]

        training_errors = nn.train_on_dataset(training_input, training_output, iterations, epochs, learning_rate)

        for i in range(len(test_output)):
            print(test_input[i].reshape(7, 5))
            print(f"expected; {test_output[i]}, got: {nn.feed_forward(test_input[i])}")

        testing_error = nn.get_error_on_dataset(test_input, test_output)

        return avg(training_errors[-1]), avg(testing_error)


def MultilayerPerceptronMnistRecognizeNumber(probability, hidden_layer_nodes: int = 30, iterations=100, epochs=30, learning_rate=0.1):
    nn = NNBuilder \
        .with_input(7*5) \
        .with_hidden_layer(hidden_layer_nodes, sigmoid, sigmoid_derived) \
        .with_output_layer(10, sigmoid, sigmoid_derived)

    with open("numbers.txt", 'r') as file:
        input = np.array(flatten_array([[float(a) for a in i.replace("\n","").split(' ')] for i in file.readlines()]))

        digits_input = input.reshape((10, 7*5))

        dataset = []
        results = []

        for i in range(10):
            digit = digits_input[i]
            dataset.append(digit)
            expected = [1 if i == j else 0 for j in range(10)]
            results.append(expected)

        training_input, training_output = shuffle_data(dataset, results)
        test_input = []

        for d in dataset:
            d_with_noise = np.array([i if random.uniform(0, 1) > probability else (i+1) % 2 for i in d])  # noise
            test_input.append(d_with_noise)

        test_output = results

        training_errors = nn.train_on_dataset(training_input, training_output, iterations, epochs, learning_rate)

        for i in range(len(test_output)):
            print(test_input[i].reshape(7, 5))
            print(f"expected; {test_output[i]}, got: {nn.feed_forward(test_input[i])}")

        testing_error = nn.get_error_on_dataset(test_input, test_output)
        return avg(training_errors[-1]), avg(testing_error)
