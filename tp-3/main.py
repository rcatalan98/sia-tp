import numpy as np

import Plots

from Ej1 import SimplePerceptronAnd, SimplePerceptronOr, SimplePerceptronXor
from Ej2 import LinearPerceptron, NotLinearPerceptron
from Ej3 import MultilayerPerceptronXor, MultilayerPerceptronMnistEvenOrOdd, MultilayerPerceptronMnistRecognizeNumber


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
    iterations = [1, 5, 10, 25, 50, 75, 100, 150, 200]  # former epoch_size
    xor_epochs = 600
    mnist_epochs = 100

    # xor --> hidden_layer_nodes=5, epochs=600, iterations=75, learning_rate=0.7
    results_xor = np.array([MultilayerPerceptronXor(epochs=xor_epochs, iterations=it) for it in iterations])

    # even_or_odd --> hidden_layer_nodes = 30, epochs = 100, iterations = 30, learning_rate = 0.1
    results_even = np.array([MultilayerPerceptronMnistEvenOrOdd(
        epochs=mnist_epochs, iterations=it) for it in iterations])

    # recognize_number --> hidden_layer_nodes=30, epochs=100, iterations=30, learning_rate=0.1
    results_recognize = np.array([MultilayerPerceptronMnistRecognizeNumber(
        probability=0.2, epochs=mnist_epochs, epoch_size=it) for it in iterations])

    # plots
    Plots.iterations_vs_error_training(iterations, results_xor, xor_epochs, "Multilayer perceptron xor")
    Plots.iterations_vs_error_training(iterations, results_even, mnist_epochs, "Multilayer perceptron even or odd")
    Plots.iterations_vs_error_training(iterations, results_recognize, mnist_epochs, "Multilayer perceptron recognize number")
    Plots.iterations_vs_error_testing(iterations, results_xor, xor_epochs, "Multilayer perceptron xor")
    Plots.iterations_vs_error_testing(iterations, results_even, mnist_epochs, "Multilayer perceptron even or odd")
    Plots.iterations_vs_error_testing(iterations, results_recognize, mnist_epochs, "Multilayer perceptron recognize number")

    # Plots.epoch_vs_metric(results[], xor_epochs, , f'Multilayer perceptron xor {}')

    # ws = MultilayerPerceptronMnistRecognizeNumber(probability=0.02,)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ej1()
    # ej2()
    ej3()
