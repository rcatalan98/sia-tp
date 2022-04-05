import random
from math import ceil
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


def get_rank_fitness(rank: int, population_size: int) -> float:
    return (population_size - 1 - rank) / population_size


class RankSelection(BaseSelection):

    def select(self, population: List[Bag]) -> List[Bag]:
        population.sort(key=self.sort_by_fitness, reverse=True)
        population_size = ceil(len(population) / 2)
        return random.choices(
            population,
            weights=[get_rank_fitness(i, population_size) for i, p in enumerate(population)],
            k=population_size
        )
