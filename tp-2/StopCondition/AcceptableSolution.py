from __future__ import annotations

from typing import Dict

from StopCondition.BaseStopCondition import BaseStopCondition


class AcceptableSolution(BaseStopCondition):

    def __init__(self, pool_manager, acceptable_benefit: int):
        super().__init__(pool_manager)
        self.acceptable_benefit: int = acceptable_benefit

    def has_to_stop(self):
        return max([p.fitness for p in self.pool_manager.population]) >= self.acceptable_benefit

