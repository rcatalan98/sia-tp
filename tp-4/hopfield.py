import math
import numpy as np


class Hopfield:
    def __init__(self, patterns):
        # 1 - almacenar los patrones conocidos
        self.stored_patterns = np.array(patterns)
        self.N = len(patterns[0])   # dimension de los patrones

        # 2 - calcular los pesos sinapticos
        # W = 1/N * K' * K - I  (K matriz con los patrones en las filas)
        self.w = np.dot(self.stored_patterns.T, self.stored_patterns) / self.N
        np.fill_diagonal(self.w, 0)

    def run(self, query_pattern):
        # 3 - vector de estados iniciales S(0)
        states = np.array(query_pattern)
        prev_states = np.zeros(self.N)

        # 4 - iteracion hasta la convergencia: actualizar el vector S(t) hasta que permanezca estable
        # Los pesos permanecen fijos y en cada paso cambian los estados
        while not np.array_equal(states, prev_states):  # TODO: max iterations?
            # TODO: print states
            prev_states = states
            states = self.next_states(states)

        # 5 - salida: el patron asociado al ultimo estado calculado
        spurious_state = True

        for pattern in self.stored_patterns:
            if np.array_equal(pattern, states):
                spurious_state = False
                break

        return states, spurious_state

    def next_states(self, current_states):
        next_states = np.zeros(self.N)

        for i in range(self.N):
            sum = 0
            for j in range(self.N):
                if not j == i:
                    sum += self.w[i][j] * current_states[j]
            next_states[i] = math.fabs(sum)

        return next_states
