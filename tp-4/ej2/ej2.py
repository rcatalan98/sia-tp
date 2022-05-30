import random
import numpy as np

from ej2.hopfield import Hopfield
from ej2.letters import get_letters_patterns
from ej2.utils import print_pattern
import ej2.plots as plots


def ej2():
    probability_list = [0.02, 0.05, 0.1, 0.2, 0.3, 0.4]
    letter_list = ['A', 'L', 'T', 'X']
    times = 100

    patterns = get_letters_patterns(letter_list)
    hopfield = Hopfield(patterns)

    dictionary = {}

    for i in range(len(patterns)):
        dictionary[letter_list[i]] = {}
        for probability in probability_list:
            inner_dictionary = {
                    "pattern": patterns[i],
                    "hopfield_run": [],
                    "total_spurious_states": 0,
                    "iterations_avg": 0
            }
            iter_avg = 0
            total_spurious_states = 0
            for t in range(times):
                iterations = 100
                while iterations > 15:  # el ayudante dijo que ignoremos los casos en los que no converge rapido
                    pattern_with_noise = noise(patterns[i], probability)    # returns a new array doesn't modify patterns[i]
                    output_pattern, spurious_state, iterations, energies = hopfield.run(pattern_with_noise, print_states=False)

                iter_avg += iterations
                aux = {
                    "pattern_with_noise": pattern_with_noise,
                    "output_pattern": output_pattern,
                    "spurious_state": spurious_state,
                    "iterations": iterations,
                    "energies": energies
                }
                inner_dictionary.get("hopfield_run").append(aux)

                if spurious_state:
                    total_spurious_states += 1

            inner_dictionary.update({"total_spurious_states": total_spurious_states})
            inner_dictionary.update({"iterations_avg": iter_avg / times})
            dictionary[letter_list[i]][probability] = inner_dictionary

    plot(dictionary, times)


def plot(dictionary, times):
    letter = 'A'
    probability = 0.2
    energies_list = []
    iterations_list = []

    for run in dictionary[letter][probability]["hopfield_run"]:
        energies_list.append(run["energies"])
        iterations_list.append(run["iterations"])

    suptitle = f'Evolución de la energía'
    title = f'Letra: {letter}, Probabilidad de ruido: {probability}'
    plots.energy_vs_iterations(energies_list, iterations_list, suptitle, title, times=5)

    suptitle = f'Cantidad de iteraciones promedio variando la probabilidad de ruido'
    title = f'Ejecuciones (por cada probabilidad): {times}'
    ylabel = f'Iteraciones promedio'
    plots.noise_probability_vs_data(dictionary, "iterations_avg", suptitle, title, ylabel)

    suptitle = f'Cantidad de estados espurios variando la probabilidad de ruido'
    ylabel = f'Estados espurios'
    plots.noise_probability_vs_data(dictionary, "total_spurious_states", suptitle, title, ylabel)


def noise(pattern, probability):
    noisy = np.array(pattern)
    for i in range(len(pattern)):
        noisy[i] = pattern[i] * (-1 if random.uniform(0, 1) < probability else 1)
    return noisy


def print_dictionary(dictionary):
    # print(f'\n\nprobability: {probability}')

    # print(f'letter: {letter_list[i]}\npattern:')
    # print_pattern(patterns[i], 5)

    #     print(f'{t+1} - estado espureo: {spurious_state} - iteraciones: {iterations}\n'
    #           f'patron de entrada (con ruido):')
    #     print_pattern(pattern_with_noise, 5)
    #     print(f'patron de salida:')
    #     print_pattern(output_pattern, 5)
    #     print(f'energia: {energies}')
    # print(f'total de estados espurios: {total_spurious_states}')

    print()
