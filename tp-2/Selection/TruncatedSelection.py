import random
from typing import List
from math import ceil

from Selection.BaseSelection import BaseSelection
from Bag import Bag


class TruncatedSelection(BaseSelection):
    def select(self, population: List[Bag], threshold: float = None, k: int = None) -> List[Bag]:
        p = ceil(len(population)/2)  # p can't be odd since p=len/2=2p/2
        if k < 0 or k > p:
            raise Exception("k is invalid")

        population.sort(key=self.sort_by_fitness)
        length = 2*p
        truncated: List[Bag] = population[length-k:length]

        return random.choices(truncated, k=p)
