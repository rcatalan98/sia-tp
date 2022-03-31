from typing import List

from Bag import Bag
from Breeding.BaseBreeder import BaseBreeder
from ConfigStore import ConfigStore
from Mutation.BaseMutation import BaseMutation
from Selection.BaseSelection import BaseSelection


class PoolManager:
    # Todo hace falta guardar todas las generaciones o se pisa population?
    def __init__(self, config: ConfigStore):
        self.population: List[Bag] = self.create_random_population(config, config.population_size)
        self.mutator: BaseMutation = config.get_mutator()
        self.selector: BaseSelection = config.get_selector()
        self.breeder: BaseBreeder = config.get_breeder()
        self.generation = 0

    @staticmethod
    def create_random_population(config: ConfigStore, p: int) -> List[Bag]:
        return [Bag.create_random(config) for _ in range(p)]

    def get_new_generation(self) -> List[Bag]:
        couples = self.first_selector(self.population, 2)
        children: List[Bag] = []
        for a, b in couples:
            children.extend([self.mutator.mutate(el) for el in self.breeder.breed(a, b)])
        new_generation = self.second_selector(self.population+children)
        self.generation += 1
        return new_generation
        # ToDo cuando y donde nos fijamos el corte y cuando pisar la poblacion




