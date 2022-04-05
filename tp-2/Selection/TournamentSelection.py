import random
from math import ceil
from typing import List

from Bag import Bag
from Selection.BaseSelection import BaseSelection


class TournamentSelection(BaseSelection):

    def __init__(self, threshold: float):
        self.threshold = threshold

    def run_match(self, couple: List[Bag]):
        return couple[0] if random.uniform(0, 1) < self.threshold else couple[1]

    def select(self, population: List[Bag]) -> List[Bag]:
        next_population_size = ceil(len(population) / 2)
        selection_bags: List[Bag] = []

        for i in range(next_population_size):
            first_couple: List[Bag] = sorted(
                [
                    population[random.randint(0, len(population) - 1)],
                    population[random.randint(0, len(population) - 1)]
                ],
                key=lambda b: b.fitness,
                reverse=True
            )
            second_couple: List[Bag] = sorted(
                [
                    population[random.randint(0, len(population) - 1)],
                    population[random.randint(0, len(population) - 1)]
                ],
                key=lambda b: b.fitness,
                reverse=True
            )
            final_match: List[Bag] = sorted(
                [
                    self.run_match(first_couple),
                    self.run_match(second_couple),
                ],
                key=lambda b: b.fitness,
                reverse=True
            )
            selection_bags.append(self.run_match(final_match))
        return selection_bags
