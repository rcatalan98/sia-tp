import math
import random
from typing import List, Dict

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class BoltzmannSelection(BaseSelection):

    def __init__(self, k: float, t0: float, tc: float, n_generation: int):
        self.temperature: float = tc + (t0 - tc) * math.exp(-k * n_generation)

    def boltz_fitness(self,bag: Bag):
        return math.exp(bag.fitness/self.temperature)

    def select(self, population: List[Bag]) -> List[Bag]:
        return random.choices(
            population,
            weights=[BoltzmannSelection.boltz_fitness(bag) for bag in population],
            k=math.ceil(len(population) / 2))
