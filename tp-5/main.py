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

    beta = 0.5

    # nn = NNBuilder \
    #     .with_input(7 * 5) \
    #     .with_hidden_layer(30, activation, derivative) \
    #     .with_hidden_layer(20, activation, derivative) \
    #     .with_hidden_layer(10, activation, derivative) \
    #     .with_hidden_layer(5, activation, derivative) \
    #     .with_hidden_layer(2, activation, derivative) \
    #     .with_hidden_layer(5, activation, derivative) \
    #     .with_hidden_layer(10, activation, derivative) \
    #     .with_hidden_layer(20, activation, derivative) \
    #     .with_hidden_layer(30, activation, derivative) \
    #     .with_output_layer(7 * 5, activation, derivative)

    nn = NNBuilder \
        .with_input(7 * 5) \
        .with_hidden_layer(10, activation, derivative) \
        .with_hidden_layer(2, activation, derivative) \
        .with_hidden_layer(10, activation, derivative) \
        .with_output_layer(7 * 5, activation, derivative)

    # np.random.shuffle(fonts)
    idx = math.floor(font_count * .5)
    training, test = np.array(fonts[:idx]), np.array(fonts[idx:])

    training_errors, ws, bs = nn.train_on_dataset(training, training, 15000, 0.0005)

    # print(f"training error: {training_errors[-1]}")
    # print(f"testing error: {nn.get_error_on_dataset(test, test)}")

    aa = test[0]
    value = nn.feed_forward(aa)

    print_character(aa.reshape(7, 5))

    print_character(value.reshape(7, 5))
