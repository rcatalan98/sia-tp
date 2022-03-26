from typing import List

from Bag import Bag
from Breeding.breeding_functions import chunks
from ConfigStore import ConfigStore


class PoolManager:
    # Todo hace falta guardar todas las generaciones o se pisa population?
    def __init__(self, config: ConfigStore):
        self.population: List[Bag] = self.create_random_population()
        self.mutator = config.get_mutator()
        self.selector = config.get_selector()
        self.breeder = config.get_breeder()
        self.generation = 0

    def create_random_population(self) -> List[Bag]:
        pass

    def get_new_generation(self) -> List[Bag]:
        couples = chunks(self.population, 2)
        children: List[Bag] = List[Bag]()
        for a, b in couples:
            children.extend(map(self.mutator, self.breeder(a, b)))
        new_generation = self.selector(self.population+children)
        self.generation += 1
        return new_generation
        # ToDo cuando y donde nos fijamos el corte y cuando pisar la poblacion



