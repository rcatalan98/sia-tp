from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class EliteSelection(BaseSelection):

    def select(self, population: List[Bag]) -> List[Bag]:
        population.sort(key=self.sort_by_fitness)
        return population[0:len(population)/2]
