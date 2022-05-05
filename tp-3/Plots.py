from matplotlib import pyplot as plt, colors as mcolors


def iterations_vs_error(iterations, results, epochs, title: str = None):
    css4, xkcd = get_colors(len(iterations))

    epochs_x = [i for i in range(1, epochs+1)]
    for i in range(len(iterations)):
        plt.plot(epochs_x, results[i]["training_error"], label=f"{iterations[i]} iter training", color=css4[i])
        plt.plot(epochs_x, results[i]["testing_error"], label=f"{iterations[i]} iter testing", linestyle="dotted", color=xkcd[i])

    plt.xlabel('epoch')
    plt.ylabel('error')
    plt.title(title)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()


def get_colors(n):
    # https://matplotlib.org/3.5.0/tutorials/colors/colors.html
    color_names = {"aqua", "chocolate", "coral", "crimson", "green", "magenta", "navy", "orange", "violet"}

    if n > len(color_names):
        raise "Plot error: I don't know that many colors"

    css4 = []
    xkcd = []

    for color_name in color_names:
        css4.append(mcolors.CSS4_COLORS[color_name])
        xkcd.append(mcolors.XKCD_COLORS[f'xkcd:{color_name}'])

    return css4, xkcd
