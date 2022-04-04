from __future__ import annotations

from typing import Dict

from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition
from StopCondition.TimeBased import TimeBased


class SameFitness(BaseStopCondition):

    def __init__(self, pool_manager: PoolManager, generations_with_same_fitness: int):
        super().__init__(pool_manager)
        self.generations_with_same_fitness: int = generations_with_same_fitness
        self.max_time = TimeBased(runtime_in_seconds=500, pool_manager=self)


    def has_to_stop(self):
       if len(self.pool_manager.all_fitness) <= self.generations_with_same_fitness:
           return False
       else:
            a = self.pool_manager.all_fitness[-self.generations_with_same_fitness:]
            return self.max_time.has_to_stop() or all(a[0] == i for i in a)
