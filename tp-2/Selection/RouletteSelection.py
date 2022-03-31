import random
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class RouletteSelection(BaseSelection):

    def select(self, population: List[Bag], population_size: int) -> List[Bag]:
        final_bags = random.choices(population, weights=[p.fitness for p in population], k=population_size)
        return final_bags
