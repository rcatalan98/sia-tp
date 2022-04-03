import random
from typing import List
from math import ceil

from Selection.BaseSelection import BaseSelection
from Bag import Bag


class TruncatedSelection(BaseSelection):
    def __init__(self, k: int):
        self.k = k

    def select(self, population: List[Bag]) -> List[Bag]:
        p = ceil(len(population)/2)  # p can't be odd since p=len/2=2p/2
        if self.k < 0 or self.k > p:
            raise Exception("k is invalid")

        population.sort(key=self.sort_by_fitness, reverse=True)
        length = 2*p
        truncated: List[Bag] = population[length-self.k:length]

        return random.choices(truncated, k=p)
