from __future__ import annotations

from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition


class GenerationCount(BaseStopCondition):

    def __init__(self, pool_manager: PoolManager, max_generation: int):
        super().__init__(pool_manager)
        self.max_generation: int = max_generation

    def has_to_stop(self):
        return self.max_generation <= self.pool_manager.generation
