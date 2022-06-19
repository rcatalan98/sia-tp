from time import perf_counter

from test_fonts import *
from NeuralNetwork import *

sigmoid = lambda e: 1 / (1 + np.exp(-e * 2 * beta))
sigmoid_derived = lambda e: 2 * beta * sigmoid(e) * (1 - sigmoid(e))

tanh = lambda e: math.tanh(e)
tanh_derived = lambda e: 1 - math.tanh(e) ** 2


def activation(e):
    return tanh(e)


def derivative(e):
    return tanh_derived(e)


if __name__ == '__main__':
    fonts = get_all_fonts(2, True)
    font_count = len(fonts)
    print(f'font_count: {font_count}')
    beta = 0.5

    nn = NNBuilder \
        .with_input(7 * 5) \
        .with_hidden_layer(20, activation, derivative) \
        .with_hidden_layer(10, activation, derivative) \
        .with_hidden_layer(5, activation, derivative) \
        .with_hidden_layer(2, activation, derivative) \
        .with_hidden_layer(5, activation, derivative) \
        .with_hidden_layer(10, activation, derivative) \
        .with_hidden_layer(20, activation, derivative) \
        .with_output_layer(7 * 5, activation, derivative)

    np.random.shuffle(fonts)
    idx = math.floor(font_count * 0.5)
    idx = 5
    training, test = np.array(fonts[:idx]), np.array(fonts[idx:])

    t0 = perf_counter()
    training_errors, ws = nn.train_on_dataset(training, training, 10)
    tf = perf_counter()

    print(f'execution time: {tf - t0} s')
    print(f"training error: {training_errors}")

    aa = test[0]
    value = nn.feed_forward(aa)

    print(print_character(aa.reshape(7, 5)))

    print(print_character(value.reshape(7, 5)))
