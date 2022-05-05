import math
import random
import numpy as np
from enum import Enum

import Metrics
from NeuralNetwork import NNBuilder
from Utils import flatten_array, shuffle_data, avg

sigmoid = lambda e: 1 / (1 + math.exp(-e))
sigmoid_derived = lambda e: sigmoid(e) * (1 - sigmoid(e))


def MultilayerPerceptronXor(hidden_layer_nodes: int = 5, epochs=600, iterations=75, learning_rate=0.7):
    nn = NNBuilder \
        .with_input(2) \
        .with_hidden_layer(hidden_layer_nodes, sigmoid, sigmoid_derived) \
        .with_output_layer(1, sigmoid, sigmoid_derived)

    xor_data_set = [[0, 1], [1, 0], [0, 0], [1, 1]]
    xor_expected_results = [1, 1, 0, 0]

    (training_errors, ws, bs) = nn.train_on_dataset(xor_data_set, xor_expected_results, epochs, iterations, learning_rate)

    print(training_errors[-1])
    for val in xor_data_set:
        print(f"\t{val[0]} \txor \t{val[1]} \tis \t{round(nn.feed_forward(val)[0])}")

    results = dict()
    results['training_error'] = training_errors
    results['testing_error'] = [nn.get_error_on_dataset(xor_data_set, xor_expected_results, w=ws[i], b=bs[i]) for i in range(len(ws))]

    return results


def MultilayerPerceptronMnistEvenOrOdd(hidden_layer_nodes: int = 30, epochs=100, iterations=30, learning_rate=0.1):
    nn = NNBuilder \
        .with_input(7 * 5) \
        .with_hidden_layer(hidden_layer_nodes, sigmoid, sigmoid_derived) \
        .with_output_layer(1, sigmoid, sigmoid_derived)

    with open("numbers.txt", 'r') as file:
        input = np.array(flatten_array([[float(a) for a in i.replace("\n", "").split(' ')] for i in file.readlines()]))

        digits_input = input.reshape((10, 7 * 5))

        dataset = []
        results = []

        for i in range(10):
            digit = digits_input[i]
            dataset.append(digit)
            expected = [i % 2]
            results.append(expected)

        dataset, result = shuffle_data(dataset, results)  # FIXME: pisar results? (falto la s?)

        training_input = dataset[:9]
        training_output = result[:9]
        test_input = dataset[9:]
        test_output = result[9:]

        (training_errors, ws, bs) = nn.train_on_dataset(training_input, training_output, epochs, iterations, learning_rate)

        for i in range(len(test_output)):
            print(test_input[i].reshape(7, 5))
            print(f"expected; {test_output[i]}, got: {nn.feed_forward(test_input[i])}")

        results = dict()
        results['training_error'] = training_errors
        results['testing_error'] = [nn.get_error_on_dataset(test_input, test_output, w=ws[i], b=bs[i]) for i in range(len(ws))]

        return results



def normalize_number(observed, threshold = 0.15):
    sorted = np.sort(observed)
    a = sorted[-1]
    b = sorted[-2]
    normalized = np.zeros(len(observed))
    if a - b > threshold:
        normalized[np.where(observed == a)[0][0]] = 1
    return normalized

def recognize_number_error(observed, result, threshold):
    return np.count_nonzero(result != normalize_number(observed,threshold))


def MultilayerPerceptronMnistRecognizeNumber(probability, hidden_layer_nodes: int = 30, epochs=200, epoch_size=30,
                                             learning_rate=0.1):
    nn = NNBuilder \
        .with_input(7 * 5) \
        .with_hidden_layer(hidden_layer_nodes, sigmoid, sigmoid_derived) \
        .with_output_layer(10, sigmoid, sigmoid_derived, recognize_number_error)

    with open("numbers.txt", 'r') as file:
        input = np.array(flatten_array([[float(a) for a in i.replace("\n", "").split(' ')] for i in file.readlines()]))

        digits_input = input.reshape((10, 7 * 5))

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
            d_with_noise = np.array([i if random.uniform(0, 1) > probability else (i + 1) % 2 for i in d])  # noise
            test_input.append(d_with_noise)

        test_output = results

        (training_errors, ws, bs) = nn.train_on_dataset(training_input, training_output, epochs, epoch_size,
                                                        learning_rate)

        results = dict()
        results['training_error'] = training_errors
        results['testing_error'] = [nn.get_error_on_dataset(test_input, test_output, w=ws[i], b=bs[i]) for i in
                                    range(len(ws))]

        mm = Metrics.get_base_metrics_per_epoch(nn,ws[-1],bs[-1],test_input,test_output,normalize_number)

        base_metrics = Metrics.get_base_metrics(nn,ws,bs,test_input,test_output,normalize_number)

        results['test_precision'] = np.array(Metrics.get_precision(base_metrics))
        results['test_recall'] = np.array(Metrics.get_recall(base_metrics))
        results['test_f1'] = np.array(Metrics.get_f1(results['test_precision'],results['test_recall']))

        return results












