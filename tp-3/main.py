import numpy as np

import Plots

from Ej1 import SimplePerceptronAnd, SimplePerceptronOr, SimplePerceptronXor
from Ej2 import LinearPerceptron, NotLinearPerceptron
from Ej3 import MultilayerPerceptronXor, MultilayerPerceptronMnistEvenOrOdd, MultilayerPerceptronMnistRecognizeNumber, \
    classify_result


def ej1():
    # iterations = 500, epochs = 100, learning_rate = 0.1
    print("Running exercise 1...")
    SimplePerceptronAnd()
    # SimplePerceptronOr()
    SimplePerceptronXor()


def ej2():
    print("Running exercise 2...")
    LinearPerceptron()      # iterations=500, epochs=100, learning_rate=0.0001
    NotLinearPerceptron()   # iterations=100, epochs=5000, learning_rate=0.01


def ej3():
    print("Running exercise 3...")
    epoch_sizes = [1, 5, 10, 25, 50, 75, 100, 150, 200]
    #
    # # xor --> hidden_layer_nodes=5, epochs=600, epoch_size=75, learning_rate=0.7
    # errors_xor = np.array([MultilayerPerceptronXor(epochs=e) for e in epoch_sizes])
    #
    # # even_or_odd --> hidden_layer_nodes = 30, epochs = 100, epoch_size = 30, learning_rate = 0.1
    # errors_even = np.array([MultilayerPerceptronMnistEvenOrOdd(epochs=e) for e in epoch_sizes])
    #
    # # recognize_number --> hidden_layer_nodes=30, epochs=100, epoch_size=30, learning_rate=0.1
    errors_recognize = np.array([MultilayerPerceptronMnistRecognizeNumber(probability=0.2, epoch_size=e) for e in epoch_sizes])
    #
    # print(errors_xor)
    # print(errors_even)
    # print(errors_recognize)
    #
    # # plots
    # Plots.epoch_size_vs_error(epoch_sizes, errors_xor, "Multilayer perceptron xor")
    # Plots.epoch_size_vs_error(epoch_sizes, errors_even, "Multilayer perceptron even or odd")
    # Plots.epoch_size_vs_error(epoch_sizes, errors_recognize, "Multilayer perceptron recognize number")

    # ws = MultilayerPerceptronMnistRecognizeNumber(probability=0.02,)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ej1()
    # ej2()
    ej3()
    # MultilayerPerceptronMnistEvenOrOdd(epochs=50)
