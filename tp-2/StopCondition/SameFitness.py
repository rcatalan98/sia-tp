from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition


class SameFitness(BaseStopCondition):

    def __init__(self, pool_manager: PoolManager, config):
        super().__init__(pool_manager, config)
        self.previous_best_fitness: int = 0
        self.generation_counter: int = 0

    def has_to_stop(self):
        config: SameFitnessConfig = self.config

        if max([p.fitness for p in self.pool_manager.population]) == self.previous_best_fitness:
            self.generation_counter += 1
        else:
            self.generation_counter = 0

        return self.generation_counter >= config.number_of_generations_with_same_fitness



class SameFitnessConfig:
    def __init__(self,number_of_generations_with_same_fitness: int):
        self.number_of_generations_with_same_fitness = number_of_generations_with_same_fitness