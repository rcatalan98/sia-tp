import random
from math import ceil
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class RouletteSelection(BaseSelection):

    def select(self, population: List[Bag], threshold: float = None) -> List[Bag]:
        final_bags = random.choices(population, weights=[p.fitness for p in population], k=ceil(len(population)/2))
        return final_bags
