# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

from SimplePerceptron import SimplePerceptron


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    expected_results = np.array([-1, -1, -1, 1])
    perceptron = SimplePerceptron()
    w = perceptron.train(data_set, expected_results, 100, 0.2)
    print(f'the best w: {w}')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
