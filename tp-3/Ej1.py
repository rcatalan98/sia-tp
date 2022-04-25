import random

from NeuralNetwork import NNBuilder


def SimplePerceptronAnd():
    nn = NNBuilder.with_input(2).with_output_layer(1,lambda x: 1 if x > 0 else -1, lambda x:1)

    and_data_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    and_expected_results = [-1, -1, -1, 1]

    for _ in range(50000):
        i = random.randint(0,len(and_expected_results)-1)
        nn.train(and_data_set[i],and_expected_results[i],0.1)

    for val in and_data_set:
        print(f"\t{val[0]} \tand \t{val[1]} \tis \t{nn.feed_forward(val)}")


def SimplePerceptronOr():
    nn = NNBuilder.with_input(2).with_output_layer(1,lambda x: 1 if x > 0 else -1, lambda x:1)

    and_data_set = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
    and_expected_results = [1, 1, -1, 1]

    for _ in range(50000):
        i = random.randint(0,len(and_expected_results)-1)
        nn.train(and_data_set[i],and_expected_results[i],0.1)

    for val in and_data_set:
        print(f"\t{val[0]} \tand \t{val[1]} \tis \t{nn.feed_forward(val)}")
