import math
import random
import numpy as np

from NeuralNetwork import NNBuilder
from Utils import flatten_array, shuffle_data

sigmoid = lambda e: 1 / (1 + math.exp(-e))
sigmoid_derived = lambda e: sigmoid(e) * (1 - sigmoid(e))

def MultilayerPerceptronXor():
    nn = NNBuilder\
                    .with_input(2)\
                    .with_hidden_layer(4,sigmoid, sigmoid_derived)\
                    .with_output_layer(1,sigmoid, sigmoid_derived)

    xor_data_set = [[0, 1], [1, 0], [0, 0], [1, 1]]
    xor_expected_results = [1, 1, 0, 0]

    errors = nn.train_on_dataset(xor_data_set,xor_expected_results,600,75,0.7)

    print(errors[-1])
    for val in xor_data_set:
        print(f"\t{val[0]} \txor \t{val[1]} \tis \t{round(nn.feed_forward(val)[0])}")

    return errors

def MultilayerPerceptronMnist():
    nn = NNBuilder \
        .with_input(7*5) \
        .with_hidden_layer(30, sigmoid, sigmoid_derived) \
        .with_output_layer(2, sigmoid, sigmoid_derived)

    with open("numbers.txt", 'r') as file:
        input = np.array(flatten_array([[float(a) for a in i.replace("\n","").split(' ')] for i in file.readlines()]))

        digits_input = input.reshape((10,7*5))

        dataset = []
        results = []

        for i in range(10):
            digit = digits_input[i]
            dataset.append(digit)
            expected = [1 if i % 2 == 0 else 0, 0 if i % 2 == 0 else 1]
            results.append(expected)

        dataset, result = shuffle_data(dataset,results)

        training_input = dataset[:9]
        training_output = result[:9]
        test_input = dataset[9:]
        test_output = result[9:]

        nn.train_on_dataset(training_input,training_output, 100,30,0.1)

        for i in range(len(test_output)):
            print(test_input[i].reshape(7,5))
            print(f"expected; {test_output[i]}, got: {nn.feed_forward(test_input[i])}")







