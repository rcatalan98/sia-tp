# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from Ej1 import SimplePerceptronAnd, SimplePerceptronOr
from Ej2 import LinearPerceptron, NotLinearPerceptron
from Ej3 import MultilayerPerceptronXor
from NeuralNetwork import NeuralNetwork, NNBuilder

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
    # perceptron = NotLinearPerceptron(3,4)
    #
    # with open("train_dataset.txt", 'r') as file:
    #     input = [[float(a) for a in i.split(',')] for i in file.readlines()]
    #
    # with open("expected_output.txt", 'r') as file:
    #     results = [float(i) for i in file.readlines()]
    #
    #
    # min = np.min(results)
    # max = np.max(results)
    #
    # normalized_results = [ (res - min) / (max-min) for res in results]
    #
    # training_dataset = np.array(input[:180])
    # expected_output = np.array(normalized_results[:180])
    #
    # perceptron.train(training_dataset, expected_output, 501, 0.012)
    #
    # for i in range(180,200):
    #     print(f"expected; {results[i]}, got: {perceptron.perform(input[i])}")

    # MultilayerPerceptronXor()
    # SimplePerceptronAnd()
    # SimplePerceptronOr()
    # LinearPerceptron()
    NotLinearPerceptron()
    # Ahi CREO que funciona el backtracking. Al menos no explota.
    # No se si el gradiente deberia ser un escalar, una matriz o un vector
    # falta tocar el tema de los biases, lo tengo hecho a medias pero tengo que terminar el
    # video del chabon

    # xor_data_set = np.array([[0, 1], [1, 0], [0, 0], [1, 1]])
    # xor_expected_results = np.array([1, 1, 0, 0])
    # perceptron_xor = NeuralNetwork(2, 2, 1, 0.01, 1)
    #
    # for i in range(500):
    #     perceptron_xor.train(xor_data_set, xor_expected_results)
    #     error = perceptron_xor.estimate_error(xor_data_set,xor_expected_results)
    #     print(f"error: {error}")
    #     if error < 0.001:
    #         break

    # for val in xor_data_set:
    #     # Math.abs(Math.round(result))
    #     a = abs(perceptron_xor.perform(val).flatten().round())
    #     print(f"\t{val[0]} \txor \t{val[1]} \tis \t{a}")
        # print(f"\t{val[0]} \txor \t{val[1]} \tis \t{ 'false' if perceptron_xor.perform(val) < 0.5 else 'true'}")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
