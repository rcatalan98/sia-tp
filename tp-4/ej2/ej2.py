import random
import numpy as np

from ej2.hopfield import Hopfield
from ej2.letters import get_letters_patterns
from ej2.utils import print_pattern
import ej2.plots as plots


def ej2():
    probability_list = [0.01, 0.02, 0.05, 0.1, 0.25, 0.5]
    probability_list = [0.05, 0.2]  # todo: delete
    letter_list = ['A', 'L', 'T', 'X']
    letter_list = ['A', 'L']  # todo: delete
    times = 20

    patterns = get_letters_patterns(letter_list)
    hopfield = Hopfield(patterns)

    dictionary = {}

    for i in range(len(patterns)):
        total_spurious_states = 0
        dictionary[letter_list[i]] = {}
        for probability in probability_list:
            inner_dictionary = {
                    "pattern": patterns[i],
                    "hopfield_run": [],
                    "total_spurious_states": 0,
                    "iterations_avg": 0
            }
            iter_avg = 0
            for t in range(times):
                iterations = 100
                while iterations > 15:  # el ayudante dijo que ignoremos los casos en los que no converge rapido
                    pattern_with_noise = noise(patterns[i], probability)    # returns a new array doesn't modify patterns[i]
                    output_pattern, spurious_state, iterations, energies = hopfield.run(pattern_with_noise, print_states=False)

                # TODO: print states

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
                    total_spurious_states = total_spurious_states + 1

            inner_dictionary.update({"total_spurious_states": total_spurious_states})
            inner_dictionary.update({"iterations_avg": iter_avg / times})
            dictionary[letter_list[i]][probability] = inner_dictionary

    plot(dictionary, times)


def plot(dictionary, times):
    for letter in dictionary:
        iterations_avg_list = []
        spurious_states_list = []
        probability_list = dictionary[letter].keys()

        for probability in dictionary[letter]:
            energies_and_iterations_list = []
            inner_dict = dictionary[letter][probability]
            iterations_avg_list.append(inner_dict["iterations_avg"])
            spurious_states_list.append(inner_dict["total_spurious_states"])

            for run in inner_dict["hopfield_run"]:
                energies_and_iterations_list.append((run["energies"], run["iterations"]))

            suptitle = f'Evolución de la energía'
            title = f'Letra: {letter}, Probabilidad de ruido: {probability}'
            plots.energy_vs_iterations(energies_and_iterations_list, suptitle, title)

        suptitle = f'Cantidad de iteraciones promedio variando la probabilidad de ruido'
        title = f'Letra: {letter}, Ejecuciones (por cada probabilidad): {times}'
        plots.noise_probability_vs_iterations(probability_list, iterations_avg_list, suptitle, title)

        suptitle = f'Cantidad de estados espureos variando la probabilidad de ruido'
        plots.noise_probability_vs_spurious_states(probability_list, spurious_states_list, suptitle, title)


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
    # print(f'total de estados espureos: {total_spurious_states}')

    print()
