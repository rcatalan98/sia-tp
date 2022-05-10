from matplotlib import pyplot as plt, colors as mcolors
import numpy as np


def hyperplane(w,b):
    points_x = [-1,-1,1,1]
    points_y = [-1,1,-1,1]
    plt.scatter(points_x,points_y)
    x = np.array([-1,1])
    print(w)
    m = - w[0]/w[1]
    bias = -b/w[1]
    range_x = np.array([-1,-0.5,0,0.5,1])
    plt.plot(range_x,m*range_x+bias)
    plt.draw()
    plt.show()

def testing_and_training_vs_error(iterations_or_beta, results, epochs, title: str = None, suptitle: str = None,
                                 legend_title: str = None):
    css4, xkcd = get_colors(len(iterations_or_beta)*2)

    epochs_x = [i for i in range(1, epochs + 1)]
    for i in range(len(iterations_or_beta)):
        plt.plot(epochs_x, results[i]["training_error"], label=f"Training", color=css4[i])
        plt.plot(epochs_x,results[i]["testing_error"],label=f"Testing", color=css4[i+1])

    plt.xlabel('epoch')
    plt.ylabel('error')
    plt.title(f'{title} - training set')
    plt.suptitle(suptitle)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title=legend_title)
    plt.tight_layout()
    plt.show()

def iterations_vs_error_training(iterations_or_beta, results, epochs, title: str = None, suptitle: str = None,
                                 legend_title: str = None):
    css4, xkcd = get_colors(len(iterations_or_beta))

    epochs_x = [i for i in range(1, epochs+1)]
    for i in range(len(iterations_or_beta)):
        plt.plot(epochs_x, results[i]["training_error"], label=f"{iterations_or_beta[i]}", color=css4[i])

    plt.xlabel('epoch')
    plt.ylabel('error')
    plt.title(f'{title} - training set')
    plt.suptitle(suptitle)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title=legend_title)
    plt.tight_layout()
    plt.show()


def iterations_vs_error_testing(iterations_or_beta, results, epochs, title: str = None, suptitle: str = None,
                                legend_title: str = None, one_value: bool = False):
    css4, xkcd = get_colors(len(iterations_or_beta))

    epochs_x = [i for i in range(1, epochs + 1)]
    for i in range(len(iterations_or_beta)):
        plt.plot(epochs_x, results[i]["testing_error"], label=f"{iterations_or_beta[i]}", color=xkcd[i])

    plt.xlabel('epoch')
    plt.ylabel('error')
    if one_value:
        aux = title
    else:
        aux = f'{title} - testing set'
    plt.title(aux)
    plt.suptitle(suptitle)

    if not one_value:
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title=legend_title)
    plt.tight_layout()
    plt.show()


def epoch_vs_metric(results, epochs, metric_name, title: str = None, suptitle: str = None):
    epochs_x = [i for i in range(1, epochs+1)]

    plt.plot(epochs_x, results[f'train_{metric_name}'], label=f"train")
    plt.plot(epochs_x, results[f'test_{metric_name}'], label=f"test")

    plt.xlabel('epoch')
    plt.ylabel(metric_name)
    plt.title(title)
    plt.suptitle(suptitle)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()


def epoch_vs_metric_all(iterations_or_betas, results, epochs, metric_name, title: str = None, suptitle: str = None,
                        legend_title: str = None):
    epochs_x = [i for i in range(1, epochs+1)]

    for i in range(len(iterations_or_betas)):
        plt.plot(epochs_x, results[i][f'test_{metric_name}'], label=f"{iterations_or_betas[i]}")

    plt.xlabel('epoch')
    plt.ylabel(metric_name)
    plt.title(f'{title} - testing sets')
    plt.suptitle(suptitle)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), title=legend_title)
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
