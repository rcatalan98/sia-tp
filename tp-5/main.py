from time import perf_counter

from test_fonts import *
from NeuralNetwork import *
import plots

sigmoid = lambda e: 1 / (1 + np.exp(-e * 2 * beta))
sigmoid_derived = lambda e: 2 * beta * sigmoid(e) * (1 - sigmoid(e))

tanh = lambda e: math.tanh(e)
tanh_derived = lambda e: 1 - math.tanh(e) ** 2


def activation(e):
    return tanh(e)


def derivative(e):
    return tanh_derived(e)


if __name__ == '__main__':
    chosen_dataset = 2
    fonts = get_all_fonts(chosen_dataset, True)
    font_count = len(fonts)
    print(f'font_count: {font_count}')
    beta = 0.5

    nn = NNBuilder \
        .with_input(7 * 5) \
        .with_hidden_layer(20, activation, derivative) \
        .with_hidden_layer(10, activation, derivative) \
        .with_hidden_layer(2, activation, derivative) \
        .with_hidden_layer(10, activation, derivative) \
        .with_hidden_layer(20, activation, derivative) \
        .with_output_layer(7 * 5, activation, derivative)

    # np.random.shuffle(fonts)
    idx = math.floor(font_count * 0.5)
    idx = 5
    input_fonts = np.array(fonts[:idx])
    expected_output = input_fonts

    t0 = perf_counter()
    training_errors, ws = nn.train_on_dataset(input_fonts, expected_output, 20)
    tf = perf_counter()

    print(f'execution time: {tf - t0} s')
    print(f"training error: {training_errors}")

    # FIXME: con el shuffle las labels no se corresponden
    labels = [
        ["space", "!", "\"", "#", "$", "%", "&", "\'", "(", ")", "*", "+",
         ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
         ":", ";", "<", "=", ">", "?"],
        ["@", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
         "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_"]
    ]

    outputs = []
    latent_space_list = []
    latent_space_layer = int(np.ceil(nn.layer_count / 2))

    for font in input_fonts:
        layers_outputs = nn.feed_forward(font)
        outputs.append(layers_outputs[-1])
        latent_space_list.append(layers_outputs[latent_space_layer])

        # print(print_character(font.reshape(7, 5)))
        # print(print_character(layers_outputs[-1].reshape(7, 5)))

    plots.plot_latent_space(latent_space_list, labels[chosen_dataset - 1])

    print()
