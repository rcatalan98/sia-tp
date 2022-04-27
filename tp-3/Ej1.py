import random

from NeuralNetwork import NNBuilder


def SimplePerceptronAnd():
    nn = NNBuilder.with_input(2).with_output_layer(1,lambda x: 1 if x > 0 else -1, lambda x: 1)

    and_data_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    and_expected_results = [-1, -1, -1, 1]

    nn.train_on_dataset(and_data_set,and_expected_results, 500, 100, 0.1)

    for val in and_data_set:
        print(f"\t{val[0]} \tand \t{val[1]} \tis \t{nn.feed_forward(val)}")


def SimplePerceptronOr():
    nn = NNBuilder.with_input(2).with_output_layer(1,lambda x: 1 if x > 0 else -1, lambda x: 1)

    or_data_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    or_expected_results = [1, 1, -1, 1]

    nn.train_on_dataset(or_data_set,or_expected_results,500,100,0.1)

    for val in or_data_set:
        print(f"\t{val[0]} \tor \t{val[1]} \tis \t{nn.feed_forward(val)}")


def SimplePerceptronXor():
    nn = NNBuilder.with_input(2).with_output_layer(1,lambda x: 1 if x > 0 else -1, lambda x:1)

    or_data_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    or_expected_results = [1, 1, -1, -1]

    nn.train_on_dataset(or_data_set,or_expected_results, 500, 100, 0.1)

    for val in or_data_set:
        print(f"\t{val[0]} \txor \t{val[1]} \tis \t{nn.feed_forward(val)}")
