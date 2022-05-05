from enum import Enum
import numpy as np


class Result(Enum):
    TRUE_POSITIVE = 1
    FALSE_POSITIVE = 2
    TRUE_NEGATIVE = 3
    FALSE_NEGATIVE = 4


def is_positive(nn_says, current_number):
    return np.count_nonzero(nn_says != current_number) == 0


def is_true(nn_says, input):
    return np.count_nonzero(nn_says != input) == 0


def classify_result(current_number, input_number, nn_says):
    true = is_true(nn_says, input_number)
    positive = is_positive(nn_says, current_number)

    if true and positive:
        return Result.TRUE_POSITIVE
    elif not true and positive:
        return Result.FALSE_POSITIVE
    elif true and not positive:
        return Result.TRUE_NEGATIVE
    elif not true and not positive:
        return Result.FALSE_NEGATIVE


def get_base_metrics_per_epoch(nn, w, b, dataset_input, dataset_output, normalize_func):
    results = []
    for i in range(10):
        current_number = np.zeros(9)
        current_number[i] = 1
        current_number = current_number.reshape(9, 1)
        for t in range(len(dataset_input)):
            input_number = dataset_output[t]
            nn_says = normalize_func(nn.feed_forward(dataset_input[t], w=w, b=b))
            results.append(classify_result(current_number, input_number, nn_says))

    d = dict()
    d[Result.TRUE_POSITIVE] = len([a for a in results if a == Result.TRUE_POSITIVE])
    d[Result.TRUE_NEGATIVE] = len([a for a in results if a == Result.TRUE_NEGATIVE])
    d[Result.FALSE_POSITIVE] = len([a for a in results if a == Result.FALSE_POSITIVE])
    d[Result.FALSE_NEGATIVE] = len([a for a in results if a == Result.FALSE_NEGATIVE])

    return d


# Devuelve una lista de diccionarios (cada diccionario representa una epoca)
# donde cada diccionario tiene informacion sobre la cantidad de falsos/verdaderos positivos/negativos
def get_base_metrics(nn, ws, bs, dataset_input, dataset_output, normalize_func):
    results = []
    for i in range(len(ws)):
        epoch_result = get_base_metrics_per_epoch(nn, ws[i], bs[i], dataset_input, dataset_output, normalize_func)
        results.append(epoch_result)

    return results


def get_precision(base_metrics):
    return [m[Result.TRUE_POSITIVE] / (m[Result.TRUE_POSITIVE] + m[Result.FALSE_POSITIVE]) for m in base_metrics]

def get_recall(base_metrics):
    return [m[Result.TRUE_POSITIVE] / (m[Result.TRUE_POSITIVE] + m[Result.FALSE_NEGATIVE]) for m in base_metrics]

def get_f1(precision,recall):
    return [(2*precision[i]*recall[i])/(precision[i]+recall[i]) for i in range(len(precision))]