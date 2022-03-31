import random
from copy import deepcopy
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class TournamentSelection(BaseSelection):

    def select(self, population: List[Bag], population_size: int, threshold: float = None) -> List[Bag]:
        aux_population: List[Bag] = deepcopy(population)
        selection_bags: List[Bag] = []
        for i in range(0, population_size - 1):
            p1: Bag = aux_population.pop(random.randint(0, len(population) - 1))
            p2: Bag = aux_population.pop(random.randint(0, len(population) - 1))
            selection_bags.append(p1 if p1.fitness >= p2.fitness else p2)
        return selection_bags
