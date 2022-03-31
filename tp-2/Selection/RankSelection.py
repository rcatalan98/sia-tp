import random
from math import ceil
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


def get_rank_fitness(rank: int, population_size: int) -> float:
    return (population_size - 1 - rank) / population_size


def f_rank(bag: Bag) -> int:
    return bag.fitness


class RankSelection(BaseSelection):

    def select(self, population: List[Bag], threshold: float = None) -> List[Bag]:
        population.sort(key=f_rank)
        population_size = ceil(len(population)/2)
        final_bags = random.choices(population, weights=[get_rank_fitness(i, population_size)
                                                         for i, p in enumerate(population)],
                                    k=population_size)
        return final_bags
