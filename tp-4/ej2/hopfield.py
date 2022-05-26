import numpy as np

from ej2.utils import print_pattern, sign


class Hopfield:
    def __init__(self, patterns):
        # 1 - almacenar los patrones conocidos
        self.stored_patterns = np.array(patterns)
        self.N = len(patterns[0])   # dimension de los patrones

        # 2 - calcular los pesos sinapticos
        # W = 1/N * K' * K - I  (K matriz con los patrones en las filas)
        self.w = np.dot(self.stored_patterns.T, self.stored_patterns) / self.N
        np.fill_diagonal(self.w, 0)

    def run(self, query_pattern, print_states=True, max_iter=100):
        # 3 - vector de estados iniciales S(0)
        states = np.array(query_pattern)
        prev_states = np.zeros(self.N)
        i = 0
        energies = []

        # 4 - iteracion hasta la convergencia: actualizar el vector S(t) hasta que permanezca estable
        # Los pesos permanecen fijos y en cada paso cambian los estados
        # Siempre converge pero ponemos una cota para casos borde en los cuales le toma muchos pasos
        # Dichos casos deberan ser descartados
        while not np.array_equal(states, prev_states) and i < max_iter:
            if print_states:
                print_pattern(states, 5)
            energies.append(self.calculate_energy(states))
            prev_states = states
            states = self.next_states(states)
            i += 1

        # 5 - salida: el patron asociado al ultimo estado calculado
        spurious_state = True

        for pattern in self.stored_patterns:
            if np.array_equal(pattern, states):
                spurious_state = False
                break

        return states, spurious_state, i, energies

    def next_states(self, current_states):
        next_states = np.zeros(self.N)

        for i in range(self.N):
            sum = 0
            for j in range(self.N):
                if not j == i:
                    sum += self.w[i][j] * current_states[j]
            next_states[i] = sign(sum)

        return next_states

    def calculate_energy(self, states):
        # H = -sum(j > i, Wij * Si * Sj)
        h = 0

        for i in range(self.N):
            for j in range(i + 1, self.N):
                h += self.w[i][j] * states[i] * states[j]

        return -h
