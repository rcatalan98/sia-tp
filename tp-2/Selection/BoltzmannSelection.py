import math
import random
from typing import List, Dict

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class BoltzmannSelection(BaseSelection):

    def __init__(self, k: float, t0: float, tc: float):
        self.k = k
        self.t0 = t0
        self.tc = tc
        self.current_gen = 0

    def temperature(self, n_generation: int) -> float:
        return self.tc + (self.t0 - self.tc) * math.exp(-self.k * n_generation)

    def boltz_fitness(self, bag: Bag):
        return math.exp(bag.fitness/self.temperature(self.current_gen))

    def select(self, population: List[Bag]) -> List[Bag]:
        self.current_gen += 1
        return random.choices(
            population,
            weights=[self.boltz_fitness(bag) for bag in population],
            k=math.ceil(len(population) / 2))
