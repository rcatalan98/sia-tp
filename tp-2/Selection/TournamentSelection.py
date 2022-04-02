import random
from copy import deepcopy
from math import ceil
from typing import List, Dict

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class TournamentSelection(BaseSelection):

    def __init__(self, threshold: float):
        self.threshold = threshold

    def select(self, population: List[Bag]) -> List[Bag]:
        population_size = ceil(len(population)/2)
        aux_population: List[Bag] = deepcopy(population)
        selection_bags: List[Bag] = []

        for i in range(0, population_size - 1):
            r: float = random.uniform(0, 1)
            p1: Bag = aux_population.pop(random.randint(0, len(population) - 1))
            p2: Bag = aux_population.pop(random.randint(0, len(population) - 1))
            fittest = p1 if p1.fitness >= p2.fitness else p2
            unfit = p1 if p1.fitness < p2.fitness else p2
            if r < self.threshold:
                selection_bags.append(fittest)
            else:
                selection_bags.append(unfit)
        return selection_bags
