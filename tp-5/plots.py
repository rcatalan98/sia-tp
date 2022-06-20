from matplotlib import pyplot as plt


def plot_latent_space(latent_space_list, labels):
    x = []
    y = []

    for ls in latent_space_list:
        x.append(ls[0])
        y.append(ls[1])

    plt.scatter(x, y)

    for i in range(len(x)):
        plt.annotate(labels[i], (x[i], y[i]))

    plt.title('Espacio latente')

    plt.tight_layout()
    plt.show()
