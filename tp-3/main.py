# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
from matplotlib import pyplot as plt

from Ej1 import SimplePerceptronAnd, SimplePerceptronOr, SimplePerceptronXor
from Ej2 import LinearPerceptron, NotLinearPerceptron
from Ej3 import MultilayerPerceptronXor, MultilayerPerceptronMnistEvenOrOdd, MultilayerPerceptronMnistRecognizeNumber
from NeuralNetwork import NeuralNetwork, NNBuilder

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Ej 1
    # iterations=500, epochs=100, learning_rate=0.1
    print("Running exercise 1...")
    SimplePerceptronAnd()
    # SimplePerceptronOr()
    SimplePerceptronXor()

    # Ej 2
    print("Running exercise 2...")
    LinearPerceptron()      # iterations=500, epochs=100, learning_rate=0.0001
    NotLinearPerceptron()   # iterations=100, epochs=5000, learning_rate=0.01

    # Ej3
    print("Running exercise 3...")
    MultilayerPerceptronXor()   # hidden_layer_nodes=5, iterations=600, epochs=75, learning_rate=0.7
    MultilayerPerceptronMnistEvenOrOdd()    # hidden_layer_nodes=30, iterations=100, epochs=30, learning_rate=0.1
    MultilayerPerceptronMnistRecognizeNumber(probability=0.02)  # hidden_layer_nodes=30, iterations=100, epochs=30, learning_rate=0.1

    # # lrs = [0.001,0.01]
    # epochs = [10, 50, 75, 100, 150, 200]
    # # errors = None
    # # for _ in range(10):
    #
    # aa = []
    #
    # errors = np.array([MultilayerPerceptronXor(lr) for lr in epochs])
    #
    # for i in range(len(errors)):
    #     a = errors[i].reshape(errors.shape[1],errors.shape[2])
    #     plt.plot(np.arange(100),a,label=f"{epochs[i]}")
    #
    # # plt.plot(errors)
    # plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    # plt.tight_layout()
    # plt.show()


