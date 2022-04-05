from __future__ import annotations

import time

from StopCondition.BaseStopCondition import BaseStopCondition


class TimeBased(BaseStopCondition):
    def __init__(self, pool_manager, runtime_in_seconds: int):
        super().__init__(pool_manager)
        self.start_time = time.time()
        self.runtime_in_seconds: int = runtime_in_seconds

    def has_to_stop(self):
        return (time.time() - self.start_time) >= self.runtime_in_seconds
