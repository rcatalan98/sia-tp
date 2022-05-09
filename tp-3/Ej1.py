import random

from NeuralNetwork import NNBuilder
from Plots import hyperplane


def SimplePerceptronAnd(iterations=500, epochs=100, learning_rate=0.1):
    nn = NNBuilder.with_input(2).with_output_layer(1, lambda x: 1 if x > 0 else -1, lambda x: 1)

    and_data_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    and_expected_results = [-1, -1, -1, 1]

    nn.train_on_dataset(and_data_set, and_expected_results, epoch_size=iterations, epochs=epochs,
                        learning_rate=learning_rate)
    best_w = nn.w
    final_bias = nn.bias
    print(best_w, final_bias)
    hyperplane(best_w[0][0], final_bias[0][0][0])
    for i in range(len(and_data_set)):
        val = and_data_set[i]
        print(f"\t{val[0]} \tand \t{val[1]} \treturned \t{nn.feed_forward(val)}, \texpected: {and_expected_results[i]}")


def SimplePerceptronOr(iterations=500, epochs=100, learning_rate=0.1):
    nn = NNBuilder.with_input(2).with_output_layer(1, lambda x: 1 if x > 0 else -1, lambda x: 1)

    or_data_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    or_expected_results = [1, 1, -1, 1]

    nn.train_on_dataset(or_data_set, or_expected_results, iterations, epochs, learning_rate)

    for i in range(len(or_data_set)):
        val = or_data_set[i]
        print(f"\t{val[0]} \tor \t{val[1]} \treturned \t{nn.feed_forward(val)}, \texpected: {or_expected_results[i]}")


def SimplePerceptronXor(iterations=500, epochs=100, learning_rate=0.1):
    nn = NNBuilder.with_input(2).with_output_layer(1, lambda x: 1 if x > 0 else -1, lambda x: 1)

    xor_data_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    xor_expected_results = [1, 1, -1, -1]

    nn.train_on_dataset(xor_data_set, xor_expected_results, epoch_size=iterations, epochs=epochs, learning_rate=learning_rate)
    best_w = nn.w
    final_bias = nn.bias
    hyperplane(best_w[0][0], final_bias[0][0][0])
    for i in range(len(xor_data_set)):
        val = xor_data_set[i]
        print(f"\t{val[0]} \txor \t{val[1]} \treturned \t{nn.feed_forward(val)}, \texpected: {xor_expected_results[i]}")
