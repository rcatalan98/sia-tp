import random
from copy import deepcopy
from typing import List, Tuple

from Bag import Bag


class BaseSelection:
    def select(self, population: List[Bag]) -> List[Bag]:
        pass

    def sort_by_fitness(self, bag: Bag):
        return bag.fitness

    def get_random_couples(self, population: List[Bag]) -> List[Tuple[Bag, Bag]]:
        aux: List[Bag] = deepcopy(population)
        couples: List[Tuple[Bag, Bag]] = []

        if len(population) % 2 != 0:  # odd number of subjects
            (b1, b2) = self.get_couple(aux)
            couples.append((b1, b2))
            aux.remove(b1)  # b2 will be reused once

        while len(aux) > 0:
            (b1, b2) = self.get_couple(aux)
            couples.append((b1, b2))
            aux.remove(b1)
            aux.remove(b2)

        return couples

    def get_couple(self, population: List[Bag]) -> Tuple[Bag, Bag]:
        r1 = 0
        r2 = 0
        while r1 == r2:  # just in case randint returns the same value both times
            # random.randint incluye tanto el inicio como el final
            r1 = random.randint(0, len(population) - 1)
            r2 = random.randint(0, len(population) - 1)

        # En algun momento, esto tira error
        try:
            return population[r1], population[r2]
        except IndexError:
            raise IndexError("Invalid index")
