# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np

from NotLinearPerceptron import NotLinearPerceptron

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # and_data_set = np.array([[-1, 1], [1, -1], [-1, -1], [1, 1]])
    # and_expected_results = np.array([-1, -1, -1, 1])
    # perceptron_and = SimplePerceptron()
    # perceptron_and.train(and_data_set, and_expected_results, 100, 0.2)
    #
    # for val in and_data_set:
    #     print(f"\t{val[0]} \tand \t{val[1]} \tis \t{perceptron_and.perform(val)}")
    #
    # xor_data_set = np.array([[-1,1],[1,-1],[-1,-1],[1,1]])
    # xor_expected_results = np.array([1,1,-1,-1])
    # perceptron_xor = SimplePerceptron()
    # perceptron_xor.train(xor_data_set,xor_expected_results,100,0.9)
    #
    # for val in xor_data_set:
    #     print(f"\t{val[0]} \tand \t{val[1]} \tis \t{perceptron_xor.perform(val)}")
    perceptron = NotLinearPerceptron(3,2)

    with open("train_dataset.txt", 'r') as file:
        input = [[float(a) for a in i.split(',')] for i in file.readlines()]

    with open("expected_output.txt", 'r') as file:
        results = [float(i) for i in file.readlines()]

    training_dataset = np.array(input)
    expected_output = np.array(results)

    perceptron.train(training_dataset, expected_output, 4000, 0.01)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
