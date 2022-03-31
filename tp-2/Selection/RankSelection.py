import random
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


def get_rank_fitness(rank: int, population_size: int) -> float:
    return (population_size - 1 - rank) / population_size


def rank(bag: Bag) -> int:
    return bag.fitness


class RankSelection(BaseSelection):

    def select(self, population: List[Bag], population_size: int) -> List[Bag]:
        population.sort(key=rank)
        final_bags = random.choices(population, weights=[get_rank_fitness(i, population_size)
                                                         for i, p in enumerate(population)],
                                    k=population_size)
        return final_bags
