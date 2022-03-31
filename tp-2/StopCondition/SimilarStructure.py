from typing import Set

from Bag import Bag
from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition


class SimilarStructure(BaseStopCondition):

    def __init__(self, pool_manager: PoolManager, config):
        super().__init__(pool_manager, config)
        self.similar_generations = 0
        self.previous_generation = set()

    def has_to_stop(self):
        config: SimilarStructureConfig = self.config
        intersection: Set[Bag] = self.previous_generation.intersection(self.pool_manager.population)

        if float(len(intersection) / len(self.previous_generation)) >= config.similarity_percentage:
            self.similar_generations += 1
        else:
            self.similar_generations = 0
        # TODO: Puede que esto se rompa por el tema de refrencias, y que tengamos que copiarlo en vez de asignarlo
        self.previous_generation = self.pool_manager.population

        return self.similar_generations >= config.number_of_similar_generations


class SimilarStructureConfig:
    def __init__(self, similarity_percentage: float, number_of_similar_generations: int):
        self.similarity_percentage = similarity_percentage
        self.number_of_similar_generations = number_of_similar_generations
