import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable


def draw_countries_in_neurons_with_text(groups):
    cell_text = []

    for row in groups:
        cell_text.append([str.join("\n", item) for item in row])

    plt.figure(linewidth=2, figsize=(5, 5))
    the_table = plt.table(cellText=cell_text, cellLoc='center', loc='center')
    the_table.scale(1, 4)  # Hide axes
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)  # Hide axes border
    plt.box(on=None)
    plt.draw()
    fig = plt.gcf()
    plt.show()


def draw_countries_in_neurons(groups):
    groups = np.vectorize(lambda x: len(x))(groups)
    kohonen_net_size = groups.shape[0]
    plt.figure(figsize=groups.shape)
    plt.xticks(np.arange(float(kohonen_net_size)))
    plt.yticks(np.arange(float(kohonen_net_size)))
    # plt.title("Cantidad de registros que van en cada nodo")

    im = plt.imshow(groups)
    divider = make_axes_locatable(plt.gca())
    cax = divider.append_axes('right', size='5%', pad=0.05)
    plt.colorbar(im, cax=cax, orientation='vertical')
    plt.show()

def draw_avg_distance(kohonen_net_size, distance_matrix):
    plt.figure(figsize=(kohonen_net_size , kohonen_net_size ))
    plt.xticks(np.arange(float(kohonen_net_size)))
    plt.yticks(np.arange(float(kohonen_net_size)))
    # plt.title("Distancia promedio entre una neurona y sus vecinas")
    im = plt.imshow(np.squeeze(distance_matrix))
    divider = make_axes_locatable(plt.gca())
    cax = divider.append_axes('right', size='5%', pad=0.05)
    plt.colorbar(im, cax=cax, orientation='vertical')
    plt.show()


def draw_umatrix_per_feature(features,net,kohonen_net_size):
    fig, axs = plt.subplots(4, 2, figsize=(20, 40))
    get_dual_index = lambda x: (int(x / 2), int(x % 2))
    fig.delaxes(axs[get_dual_index(7)])

    for i, header in enumerate(features):
        data = net.distance_matrix_by_feature(i);
        chart = axs[get_dual_index(i)]
        chart.set_title(header)
        im = chart.imshow(np.squeeze(data))
        divider = make_axes_locatable(chart)
        cax = divider.append_axes('right', size='5%', pad=0.05)
        fig.colorbar(im, cax=cax, orientation='vertical')
        chart.set_xticks(np.arange(kohonen_net_size))
        chart.set_yticks(np.arange(kohonen_net_size))
        chart.xaxis.tick_top()
    plt.show()