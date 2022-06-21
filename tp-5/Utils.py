from copy import deepcopy

import numpy as np


def shuffle_data(input_dataset, result_dataset):
    data = [(input_dataset[i], result_dataset[i]) for i in range(len(result_dataset))]
    np.random.shuffle(data)
    training_data_input = [d[0] for d in data]
    training_data_output = [d[1] for d in data]
    return training_data_input, training_data_output


def normalize_array(array):
    min = np.min(array)
    max = np.max(array)

    return [(res - min) / (max - min) for res in array]


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def flatten_array(arr):
    return [item for sublist in arr for item in sublist]


def avg(arr):
    return sum(arr) / len(arr)


def create_noise(fonts, probability):
    noise_input = deepcopy(fonts)
    for font in noise_input:
        for i in range(0, len(font)):
            r = np.random.uniform(0, 1)
            if r <= probability:
                if font[i] == 1:
                    font[i] = 0
                else:
                    font[i] = 1
    return noise_input


def create_noise_gauss(fonts, probability):
    iterate = deepcopy(fonts)
    to_return = []
    for font in iterate:
        f = []
        for i in range(0, len(font)):
            r = np.random.uniform(0, 1)
            noise = 0
            if r <= probability:
                noise = np.random.normal(0, 0.1, 1)
                noise = abs(noise)
            f.append(font[i] + noise)
        to_return.append(np.array(f, dtype=float))
    return np.array(to_return)


def create_noise2(fonts, changes):
    fonts = fonts.copy().astype(float)
    for f in fonts:
        i = np.random.choice(len(f), changes, replace=False)
        noise = np.random.normal(0, 0.1, len(f))
        print(i)
        f[i] += noise
    return fonts
