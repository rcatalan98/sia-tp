from __future__ import annotations

from StopCondition.BaseStopCondition import BaseStopCondition
from StopCondition.TimeBased import TimeBased


class AcceptableSolution(BaseStopCondition):

    def __init__(self, pool_manager, acceptable_benefit: int):
        super().__init__(pool_manager)
        self.acceptable_benefit: int = acceptable_benefit
        self.max_time = TimeBased(runtime_in_seconds=50, pool_manager=self)

    def has_to_stop(self):
        return self.max_time.has_to_stop() or max(
            [p.fitness for p in self.pool_manager.population]) >= self.acceptable_benefit
