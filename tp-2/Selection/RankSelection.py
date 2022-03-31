import random
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


def get_rank_fitness(bag: Bag, population_size: int) -> int:
    return (population_size - 1 - bag.fitness) / population_size


class RankSelection(BaseSelection):

    def select(self, population: List[Bag], population_size: int) -> List[Bag]:
        final_bags = random.choices(population, weights=[get_rank_fitness(p.fitness, population_size)
                                                         for p in population],
                                    k=population_size)
        return final_bags
