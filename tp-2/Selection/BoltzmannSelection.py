import math
import random
from typing import List, Dict

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class BoltzmannSelection(BaseSelection):

    @staticmethod
    def boltz_fitness(bag: Bag, t: float):
        return math.exp(bag.fitness/t)

    def select(self, population: List[Bag], threshold: float = None, k: int = None, arg_boltz: Dict[str, float] = None) -> \
            List[Bag]:
        if arg_boltz is None or len(arg_boltz) != 4:
            raise 'Boltzmann initial arguments are missing'
        t0 = arg_boltz['t0']
        tc = arg_boltz['tc']
        k = arg_boltz['k']
        n_generation = arg_boltz['n_generation']
        temperature: float = tc + (t0 - tc) * math.exp(-k*n_generation)

        final_bags = random.choices(population, weights=[BoltzmannSelection.boltz_fitness(p, temperature)
                                                         for p in population], k=math.ceil(len(population) / 2))
        return final_bags
