from __future__ import annotations

from statistics import mean, median
from typing import List

from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition
from StopCondition.TimeBased import TimeBased


class SimilarStructure(BaseStopCondition):

    def __init__(self, pool_manager: PoolManager, similarity_percentage: float, number_of_similar_generations: int):
        super().__init__(pool_manager)
        self.similar_generations: int = 0
        self.previous_means: List[int] = []
        self.similarity_percentage: float = similarity_percentage
        self.number_of_similar_generations: int = number_of_similar_generations
        self.max_time = TimeBased(runtime_in_seconds=500, pool_manager=self)

    def has_to_stop(self):
        new_median: int = median([b.fitness for b in self.pool_manager.population])

        if len(self.previous_means) <= self.number_of_similar_generations:
            self.previous_means.append(new_median)
            return False

        generations_to_consider: List[int] = self.previous_means[-self.number_of_similar_generations:]

        mean_of_medians: float = mean(generations_to_consider)

        if mean_of_medians * self.similarity_percentage <= new_median <= mean_of_medians / self.similarity_percentage:
            return True
        else:
            self.previous_means.append(new_median)
            return self.max_time.has_to_stop()
