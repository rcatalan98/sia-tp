import random
from typing import List, Tuple

from Bag import Bag
from Breeding.BaseBreeder import BaseBreeder
from Mutation.Mutation import Mutation
from Selection.BaseSelection import BaseSelection
from StopCondition.BaseStopCondition import BaseStopCondition


class PoolManager:
    def __init__(self, config):
        self.population: List[Bag] = self.create_random_population(config)
        self.mutator: Mutation = Mutation(config.mutation_rate)
        self.selector: BaseSelection = config.get_selector()
        self.breeder: BaseBreeder = config.get_breeder()
        self.stop_condition: BaseStopCondition = config.get_stop_condition(self)
        self.generation = 0

    @staticmethod
    def create_random_population(config) -> List[Bag]:
        return [Bag.create_random(config) for _ in range(config.population_size)]

    def get_new_generation(self) -> List[Bag]:

        couples: List[Tuple[Bag, Bag]] = self.selector.get_random_couples(self.population)  #

        children: List[Bag] = []
        for (a, b) in couples:
            # children.extend(self.breeder.breed(a, b))
            children.extend([self.mutator.mutate(el) for el in self.breeder.breed(a, b)])

        # Si hay un pibe extra, matamos a uno al azar
        if len(children) != len(self.population):
            children.pop(random.randint(0, len(children)-1))

        print([s.fitness for s in self.population])
        print([s.fitness for s in children])

        new_generation = self.selector.select(self.population + children)

        self.generation += 1
        return new_generation

    def has_reached_stop_condition(self):
        return self.stop_condition.has_to_stop()




