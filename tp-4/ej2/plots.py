from matplotlib import pyplot as plt
import numpy as np

from ej2.utils import zero_to_nan


def noise_probability_vs_data(dictionary, field_name, suptitle, title, ylabel):
    width = 0.35
    letter_list = list(dictionary.keys())
    probability_list = list(dictionary[letter_list[0]].keys())

    fig, ax = plt.subplots()
    ind = np.arange(len(probability_list))

    bottom = np.zeros(len(probability_list))

    for letter in dictionary:
        data = []
        for probability in dictionary[letter]:
            # matplotlib won't plot nan (not a number) values
            data.append(dictionary[letter][probability][field_name])
        p1 = ax.bar(ind, zero_to_nan(data), width, bottom=bottom, label=letter)
        ax.bar_label(p1, label_type='center')
        bottom += data

    plt.xlabel('Probabilidad de ruido')
    plt.ylabel(ylabel)
    aux = [n for n in probability_list]
    plt.xticks(ind, aux)

    plt.suptitle(suptitle)
    plt.title(title)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title='Letra')
    plt.tight_layout()
    plt.show()


def energy_vs_iterations(energies_list, iterations_list, suptitle, title):
    for i in range(1, len(energies_list)):
        plt.plot(range(iterations_list[i]), energies_list[i], '-o')

    plt.xlabel('Iteraciones')
    plt.ylabel('Energía')
    plt.suptitle(suptitle)
    plt.title(title)
    plt.tight_layout()
    plt.show()
