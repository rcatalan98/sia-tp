import math

from matplotlib import pyplot as plt
def draw_pc1(data, countries):
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.xaxis.set_visible(True)
    ax.set_xlim(math.floor(min(data)), math.ceil(max(data)))

    for i, country in enumerate(countries):
        widths = data[i]
        ax.barh(country, widths, height=1, label=country)

    plt.show()