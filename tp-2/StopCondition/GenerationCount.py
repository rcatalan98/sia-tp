from __future__ import annotations

from typing import Dict

from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition


class GenerationCount(BaseStopCondition):

    def __init__(self, pool_manager: PoolManager, config: Dict[str, int | float]):
        super().__init__(pool_manager)
        self.max_generation: int = config['max generation']

    def has_to_stop(self):
        return self.max_generation <= self.pool_manager.generation


