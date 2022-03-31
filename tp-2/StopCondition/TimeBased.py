from PoolManager import PoolManager
from StopCondition.BaseStopCondition import BaseStopCondition
import time


class TimeBased(BaseStopCondition):
    def __init__(self, pool_manager: PoolManager, config):
        super().__init__(pool_manager, config)
        self.start_time = time.time()

    def has_to_stop(self):
        config: TimeBasedConfig = self.config

        return (time.time() - self.start_time) >= config.runtime_in_seconds


class TimeBasedConfig:
    def __init__(self, runtime_in_seconds: int):
        self.runtime_in_seconds = runtime_in_seconds
