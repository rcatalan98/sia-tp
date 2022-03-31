from typing import List, Tuple

from Bag import Bag
from Breeding.BaseBreeder import BaseBreeder
from ConfigStore import ConfigStore
from Mutation.Mutation import Mutation
from Selection.BaseSelection import BaseSelection
from StopCondition.BaseStopCondition import BaseStopCondition


class PoolManager:
    # Todo hace falta guardar todas las generaciones o se pisa population?
    def __init__(self, config: ConfigStore):
        self.population: List[Bag] = self.create_random_population(config, config.population_size)
        self.mutator: Mutation = config.get_mutator()
        self.selector: BaseSelection = config.get_selector()
        self.breeder: BaseBreeder = config.get_breeder()
        self.stop_condition: BaseStopCondition = config.get_stop_condition(self)
        self.generation = 0

    @staticmethod
    def create_random_population(config: ConfigStore, p: int) -> List[Bag]:
        return [Bag.create_random(config) for _ in range(p)]

    def get_new_generation(self) -> List[Bag]:
        couples: List[Tuple[Bag, Bag]] = self.selector.get_random_couples(self.population)  #
        children: List[Bag] = []
        for a, b in couples:
            children.extend([self.mutator.mutate(el) for el in self.breeder.breed(a, b)])
        two_p = self.population + children
        if len(children) != len(self.population):
            raise 'ERROR: the amount of children should be equal to the existing population.'
        new_generation = self.selector(two_p)
        self.generation += 1
        return new_generation
        # ToDo cuando y donde nos fijamos el corte y cuando pisar la poblacion

    def has_reached_stop_condition(self):
        return self.stop_condition.has_to_stop()




