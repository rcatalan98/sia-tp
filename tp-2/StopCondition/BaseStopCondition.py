from __future__ import annotations




class BaseStopCondition:
    def __init__(self, pool_manager):
        self.pool_manager = pool_manager

    def has_to_stop(self):
        pass
