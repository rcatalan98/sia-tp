import math
import random
import numpy as np

from NeuralNetwork import NNBuilder

sigmoid = lambda e: 1 / (1 + math.exp(-e))
sigmoid_derived = lambda e: sigmoid(e) * (1 - sigmoid(e))

def MultilayerPerceptronXor():
    nn = NNBuilder\
                    .with_input(2)\
                    .with_hidden_layer(2,sigmoid, sigmoid_derived)\
                    .with_output_layer(1,sigmoid, sigmoid_derived)

    xor_data_set = [[0, 1], [1, 0], [0, 0], [1, 1]]
    xor_expected_results = [1, 1, 0, 0]

    for _ in range(50000):
        i = random.randint(0,len(xor_expected_results)-1)
        nn.train(xor_data_set[i],xor_expected_results[i], 0.1)

    for val in xor_data_set:
        print(f"\t{val[0]} \txor \t{val[1]} \tis \t{nn.feed_forward(val)}")