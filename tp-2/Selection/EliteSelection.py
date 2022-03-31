from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


def sort_func(bag: Bag):
    return bag.fitness


class EliteSelection(BaseSelection):

    def select(self, population: List[Bag], threshold: float = None) -> List[Bag]:
        population.sort(key=sort_func)
        return population[0:len(population)/2]
