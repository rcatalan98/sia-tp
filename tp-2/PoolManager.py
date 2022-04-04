import random
from typing import List, Tuple

from Bag import Bag
from Breeding.BaseBreeder import BaseBreeder
from Mutation.Mutation import Mutation
from Selection.BaseSelection import BaseSelection
from StopCondition.BaseStopCondition import BaseStopCondition
from StopCondition.TimeBased import TimeBased


class PoolManager:
    def __init__(self, config):
        self.population: List[Bag] = self.create_random_population(config)
        self.mutator: Mutation = Mutation(config.mutation_rate)
        self.selector: BaseSelection = config.get_selector()
        self.breeder: BaseBreeder = config.get_breeder()
        self.stop_condition: BaseStopCondition = config.get_stop_condition(self)
        self.generation = 0
        self.all_fitness: List[int] = []
        self.all_weights: List[int] = []

    @staticmethod
    def create_random_population(config) -> List[Bag]:
        return [Bag.create_random(config) for _ in range(config.population_size)]

    def get_new_generation(self) -> List[Bag]:

        couples: List[Tuple[Bag, Bag]] = self.selector.get_random_couples(self.population)  #

        children: List[Bag] = []
        for (a, b) in couples:
            children.extend([self.mutator.mutate(el) for el in self.breeder.breed(a, b)])

        # Si hay un pibe extra, matamos a uno al azar
        if len(children) != len(self.population):
            children.pop(random.randint(0, len(children)-1))

        # assert len(children) == 500
        self.population = self.selector.select(self.population + children)

        (max_fitness, weight) = max([(i.fitness, i.weight) for i in self.population], key=lambda x: x[0])
        self.all_fitness.append(max_fitness)
        self.all_weights.append(weight)
        self.generation += 1

        # assert len(self.population) == 500
        return self.population

    def has_reached_stop_condition(self):
        return self.stop_condition.has_to_stop()




