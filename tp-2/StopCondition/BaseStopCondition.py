from ConfigStore import ConfigStore
from PoolManager import PoolManager


class BaseStopCondition:
    def __init__(self, pool_manager: PoolManager, config):
        self.pool_manager = pool_manager
        self.config = config

    def has_to_stop(self):
        pass
