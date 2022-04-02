from __future__ import annotations

from typing import Dict

from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition


class SameFitness(BaseStopCondition):

    def __init__(self, pool_manager: PoolManager, generations_with_same_fitness: int):
        super().__init__(pool_manager)
        self.previous_best_fitness: int = 0
        self.generation_counter: int = 0
        self.generations_with_same_fitness: int = generations_with_same_fitness

    def has_to_stop(self):
        if max([p.fitness for p in self.pool_manager.population]) == self.previous_best_fitness:
            self.generation_counter += 1
        else:
            self.generation_counter = 0

        return self.generation_counter >= self.generations_with_same_fitness
