from __future__ import annotations

from typing import Dict

from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition


class AcceptableSolution(BaseStopCondition):

    def __init__(self, pool_manager: PoolManager, config: Dict[str, int | float]):
        super().__init__(pool_manager)
        self.acceptable_benefit: int = config["acceptable solution"]

    def has_to_stop(self):
        return max([p.fitness for p in self.pool_manager.population]) >= self.acceptable_benefit

