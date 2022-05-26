import random
import numpy as np

from ej2.hopfield import Hopfield
from ej2.letters import get_letters_patterns
from ej2.utils import print_pattern


def ej2():
    probability_list = [0.01, 0.02, 0.05, 0.1, 0.25]
    probability_list = [0.5]  # todo: delete
    letter_list = ['A', 'L', 'T', 'X']
    letter_list = ['A']  # todo: delete
    times = 20

    patterns = get_letters_patterns(letter_list)
    hopfield = Hopfield(patterns)

    for probability in probability_list:
        total_spurious_states = 0
        print(f'\n\nprobability: {probability}')
        for i in range(len(patterns)):
            print(f'letter: {letter_list[i]}\npattern:')
            print_pattern(patterns[i], 5)
            for t in range(times):
                pattern_with_noise = noise(patterns[i], probability)    # returns a new array doesn't modify patterns[i]
                output_pattern, spurious_state, iterations, energies = hopfield.run(pattern_with_noise, print_states=False)

                if spurious_state:
                    total_spurious_states = total_spurious_states + 1

                print(f'{t+1} - estado espureo: {spurious_state} - iteraciones: {iterations}\n'
                      f'patron de entrada (con ruido):')
                print_pattern(pattern_with_noise, 5)
                print(f'patron de salida:')
                print_pattern(output_pattern, 5)
            print(f'total de estados espureos: {total_spurious_states}')

    # TODO: plot noise_probability vs iterations
    # TODO: plot noise_probability vs spurious states
    # TODO: plot energy vs iterations


def noise(pattern, probability):
    noisy = np.array(pattern)
    for i in range(len(pattern)):
        noisy[i] = pattern[i] * (-1 if random.uniform(0, 1) < probability else 1)
    return noisy

