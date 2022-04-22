import math

if __name__ == '__main__':
    io_values = [[(4.4793, -4.0765, -4.0765), 0], [(-4.1793, -4.9218, 1.7664), 1], [(-3.9429, -0.7689, 4.883), 1]]

    def g(x):
        try:
            return math.e ** x / (1 + math.e ** x)
        except OverflowError:
            return 1

    def F(W, w, w0, E):
        return g(sum(
            W[j + 1] * g(sum(
                w[j][k] * E[k]
                for k in range(0, 3)
            ) - w0[j])
            for j in range(0, 2)
        ) - W[0])


    def E(W, w, w0):
        return sum((OUT - F(W, w, w0, IN)) ** 2 for (IN, OUT) in io_values)
