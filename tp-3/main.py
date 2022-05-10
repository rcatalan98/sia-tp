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
    iterations = [5, 10, 50, 75, 100, 200]
    iterations = [100]  # 200 para lineal, 100 para no lineal
    learning_rates = [0.005, 0.008, 0.01, 0.015]
    learning_rates = [0.01]     # 0.01 en ambos casos
    betas = [0.5, 0.8, 1]
    betas = [1]     # 1 para no lineal, nada para lineal
    training_ratios = [0.3, 0.5, 0.7, 0.8, 0.9]
    # training_ratios = [0.8]     # 0.8 en ambos casos
    epochs_non_linear = 50
    epochs_linear = 100

    # to define the number of iterations
    results_linear = np.array(
        [LinearPerceptron(epochs=epochs_linear, iterations=it, learning_rate=lr, training_ratio=tr_ratio)
         for it in iterations
         for lr in learning_rates
         for tr_ratio in training_ratios
         ])
    best_linear = np.array([LinearPerceptron(epochs=epochs_linear, iterations=200, learning_rate=0.01, training_ratio=0.8)])
    print("Linear Calculations ended")
    # results_non_linear = [NotLinearPerceptron(epochs=epochs_non_linear)]
    results_non_linear = np.array(
        [NotLinearPerceptron(iterations=it, learning_rate=lr, b=beta,epochs=epochs_non_linear, training_ratio=tr)
         for it in iterations
         for lr in learning_rates
         for beta in betas
         for tr in [1]
         ]
    )
    best_non_linear = np.array([NotLinearPerceptron(100, epochs_non_linear, 0.01, 1)])
    print("Non Linear Calculations ended")
    # Plots.iterations_vs_error_testing(iterations,results_linear,epochs_linear,"Linear Perceptron", "Choosing iterations", "Iterations")
    # Plots.iterations_vs_error_testing(learning_rates,results_linear,epochs_linear, "Linear Perceptron", "Choosing learning rate", "Learning Rate")
    # Plots.iterations_vs_error_testing(training_ratios,results_linear,epochs_linear, "Linear Perceptron", "Choosing training ratio", "Training Ratio")
    Plots.iterations_vs_error_testing([200], best_linear, epochs_linear, f'Iteraciones = {200}, learning rate = {0.01}',
                                      "Linear Perceptron", one_value=True)

    # Plots.iterations_vs_error_testing(iterations,results_non_linear,epochs_non_linear,"NonLinear Perceptron", "Choosing Iterations", "Iterations")
    # Plots.iterations_vs_error_testing(learning_rates, results_non_linear, epochs_non_linear, "NonLinear Perceptron", "Choosing learning rate", "Learning Rate")
    # Plots.iterations_vs_error_testing(betas, results_non_linear, epochs_non_linear, "NonLinear Perceptron", "Choosing Beta", "Beta")
    Plots.iterations_vs_error_testing([100], best_non_linear, epochs_non_linear,
                                      f'Iteraciones = {100}, learning rate = {0.01}, beta = {1}',
                                      "Non Linear Perceptron",
                                      one_value=True)
    # Plots.iterations_vs_error_testing(training_ratios,results_non_linear,epochs_non_linear,"NonLinear Perceptron", "Choosing training ratio", "Training ratio")

    # to define learning rate

    # NotLinearPerceptron()   # iterations=100, epochs=5000, learning_rate=0.01


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
    ej2()
    # ej3()
