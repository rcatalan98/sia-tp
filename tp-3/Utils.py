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
