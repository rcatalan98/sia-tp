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
    LinearPerceptron()  # iterations=500, epochs=100, learning_rate=0.0001
    NotLinearPerceptron()  # iterations=100, epochs=5000, learning_rate=0.01


def ej3():
    print("Running exercise 3...")
    iterations = [1, 5, 10, 25, 50, 75, 100, 150, 200]  # former epoch_size
    iterations = [75]  # usar 75 para xor y 50 para mnist
    xor_epochs = 75
    mnist_epochs = 100
    metrics_names = ['precision', 'recall', 'f1']
    betas = [0.5, 1, 2]
    betas = [1]  # usar 1 para los 3 casos
    learning_rates = [0.01, 0.1, 0.2, 0.5, 1]
    learning_rates = [1]  # usar 1 para xor y 0.2 para mnist

    # xor --> hidden_layer_nodes=5, epochs=600, iterations=75, learning_rate=0.7
    results_xor = np.array([
        MultilayerPerceptronXor(epochs=xor_epochs, iterations=it, b=beta, learning_rate=lr)
        for it in iterations
        for beta in betas
        for lr in learning_rates
    ])

    # even_or_odd --> hidden_layer_nodes = 30, epochs = 100, iterations = 30, learning_rate = 0.1
    results_even = np.array([MultilayerPerceptronMnistEvenOrOdd(
        epochs=mnist_epochs, iterations=it) for it in iterations])

    # recognize_number --> hidden_layer_nodes=30, epochs=100, iterations=30, learning_rate=0.1
    results_recognize = np.array([
        MultilayerPerceptronMnistRecognizeNumber(
            probability=0.02, epochs=mnist_epochs, epoch_size=it, b=beta, learning_rate=lr)
        for it in iterations
        for beta in betas
        for lr in learning_rates
    ])

    # ej 3.1 plots
    # training y testing dan lo mismo

    Plots.iterations_vs_error_testing(betas, results_xor, xor_epochs, "Multilayer perceptron xor",
                                      "Choosing beta", "Beta")

    Plots.iterations_vs_error_testing(learning_rates, results_xor, xor_epochs, "Multilayer perceptron xor",
                                      "Choosing learning rate", "Learning rate")

    # este plot lo graficamos una vez para todas las iteraciones y otra una vez definidos todos los parametros
    Plots.iterations_vs_error_testing(iterations, results_xor, xor_epochs,
                                      f'Iteraciones = {iterations[0]}, beta = {betas[0]}, learning rate = {learning_rates[0]}',
                                      "Multilayer perceptron xor", one_value=True)

    # ej 3.2 plots

    Plots.iterations_vs_error_training(iterations, results_even, mnist_epochs, "Multilayer perceptron even or odd",
                                       legend_title="Iterations")
    Plots.iterations_vs_error_testing(iterations, results_even, mnist_epochs, "Multilayer perceptron even or odd",
                                      legend_title="Iterations")

    # ej 3.3 plots

    Plots.iterations_vs_error_training(iterations, results_recognize, mnist_epochs,
                                       "Multilayer perceptron recognize number", legend_title="Iterations")
    Plots.iterations_vs_error_testing(iterations, results_recognize, mnist_epochs,
                                      "Multilayer perceptron recognize number", legend_title="Iterations")

    # one plot per it - training vs testing
    for it in range(len(iterations)):
        Plots.epoch_vs_metric(results_recognize[it], mnist_epochs, metrics_names[2],
                              f'Multilayer perceptron recognize number - {metrics_names[2]} - {iterations[it]} iter')

    # para justificar la eleccion del numero de iteraciones en ej 3.3
    Plots.epoch_vs_metric_all(iterations, results_recognize, mnist_epochs, metrics_names[2],
                              f'Multilayer perceptron recognize number - {metrics_names[2]}',
                              "Choosing iterations number", "Iterations")

    # para justificar la eleccion del beta
    Plots.epoch_vs_metric_all(betas, results_recognize, mnist_epochs, metrics_names[2],
                              f'Multilayer perceptron recognize number - {metrics_names[2]}', "Choosing beta", "Beta")

    # para justificar la eleccion del learning rate
    Plots.epoch_vs_metric_all(learning_rates, results_recognize, mnist_epochs, metrics_names[2],
                              f'Multilayer perceptron recognize number - {metrics_names[2]}',
                              "Choosing learning rate", "Learning rates")

    # con iter, beta y learning_rate fijos graficamos para distintas metricas
    for name in metrics_names:
        Plots.epoch_vs_metric(results_recognize[0], mnist_epochs, name,
                              f'Iteraciones = {iterations[0]}, beta = {betas[0]}, learning rate = {learning_rates[0]}',
                              f'Multilayer perceptron recognize number - {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # ej1()
    # ej2()
    ej3()
