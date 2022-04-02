from __future__ import annotations

from typing import Dict

from ConfigStore import ConfigStore
from PoolManager import PoolManager


class BaseStopCondition:
    def __init__(self, pool_manager: PoolManager):
        self.pool_manager = pool_manager

    def has_to_stop(self):
        pass
