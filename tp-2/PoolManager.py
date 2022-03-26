from typing import List

from Bag import Bag
from ConfigStore import ConfigStore


class PoolManager:
    def __init__(self, config: ConfigStore ):
        self.population: List[Bag] = self.create_random_population()
        self.mutator = config.get_mutator()
        self.selector = config.get_selector()
        self.breeder = config.get_breeder()
        self.generation = 0

    def create_random_population(self) -> List[Bag]:
        pass

    def breed(self):
        pass

    def mutate(self):
        pass

    def select(self):
        pass


