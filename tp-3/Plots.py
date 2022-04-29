from matplotlib import pyplot as plt


def epoch_vs_error(epochs, errors, title: str = None):
    training_errors = []
    testing_errors = []

    for i in range(len(errors)):
        training_errors.append(errors[i][0])
        testing_errors.append(errors[i][1])

    plt.plot(epochs, training_errors, label="training")
    plt.plot(epochs, testing_errors, label="testing")

    plt.xlabel('epoch')
    plt.ylabel('error')
    plt.title(title)

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.tight_layout()
    plt.show()
