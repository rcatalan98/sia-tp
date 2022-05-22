import random
import numpy as np

from hopfield import Hopfield
from letters import get_letters_patterns


def ej2():
    probability = 0.02
    letter_list = ['A', 'L', 'T', 'X']

    patterns = get_letters_patterns(letter_list)
    hopfield = Hopfield(patterns)

    for p in patterns:
        pattern_with_noise = noise(p, probability)
        pattern, spurious_state = hopfield.run(pattern_with_noise)
        # TODO: do sth with the returned values


def noise(pattern, probability):
    for i in range(len(pattern)):
        if random.uniform(0, 1) < probability:
            pattern[i] *= -1
        # else remains the same
    return pattern

