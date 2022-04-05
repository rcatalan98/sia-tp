import random
from math import ceil
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class RouletteSelection(BaseSelection):

    def select(self, population: List[Bag]) -> List[Bag]:
        return random.choices(
            population,
            weights=[p.fitness for p in population],
            k=ceil(len(population) / 2)
        )
