if __name__ == '__main__':
    print("Running...")

    in_values = [[4.4793, -4.0765, -4.0765], [-4.1793, -4.9218, 1.7664], [-3.9429, -0.7689, 4.883]]
    out_values = [0, 1, 1]

    # def F(W, w, w0, E):
    #     return g(sum(
    #         W[j + 1] * g(sum(
    #             w[j][k] * E[k]
    #             for k in range(0, 3)
    #         ) - w0[j])
    #         for j in range(0, 2)
    #     ) - W[0])
    #
    #
    # def E(W, w, w0):
    #     return sum((OUT - F(W, w, w0, IN)) ** 2 for (IN, OUT) in dataset)
