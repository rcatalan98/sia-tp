from matplotlib import pyplot as plt, colors as mcolors


def iterations_vs_error_training(iterations, results, epochs, title: str = None):
    css4, xkcd = get_colors(len(iterations))

    epochs_x = [i for i in range(1, epochs+1)]
    for i in range(len(iterations)):
        plt.plot(epochs_x, results[i]["training_error"], label=f"{iterations[i]} iter", color=css4[i])

    plt.xlabel('epoch')
    plt.ylabel('error')
    plt.title(f'{title} - training set')

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()


def iterations_vs_error_testing(iterations, results, epochs, title: str = None):
    css4, xkcd = get_colors(len(iterations))

    epochs_x = [i for i in range(1, epochs + 1)]
    for i in range(len(iterations)):
        plt.plot(epochs_x, results[i]["testing_error"], label=f"{iterations[i]} iter", color=xkcd[i])

    plt.xlabel('epoch')
    plt.ylabel('error')
    plt.title(f'{title} - testing set')

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()


# def epoch_vs_metric(results, epochs, metric_name, title: str = None):
#     epochs_x = [i for i in range(1, epochs+1)]
#
#     plt.plot(epochs_x, results[0]["training_error"], label=f"")
#     plt.plot(epochs_x, results[0]["testing_error"], label=f"")
#
#     plt.xlabel('epoch')
#     plt.ylabel(metric_name)
#     plt.title(title)
#
#     plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#     plt.tight_layout()
#     plt.show()


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
