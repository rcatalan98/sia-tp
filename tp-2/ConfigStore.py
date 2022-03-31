from __future__ import annotations

from typing import List

from Item import Item
from StopCondition.AcceptableSolution import *
from StopCondition.GenerationCount import *
from StopCondition.SameFitness import *
from StopCondition.SimilarStructure import *
from StopCondition.TimeBased import *


class ConfigStore:
    def __init__(self, file: str):
        # load file
        self.stop_condition: str = ""
        self.stop_condition_config: GenerationCountConfig | AcceptableSolutionConfig | SimilarStructureConfig | \
                                    SameFitnessConfig | TimeBasedConfig | None = None

        self.item_store: List[Item] = []
        self.max_weight = 0  # info from file
        self.max_elements = 0  # info from file
        self.population_size = 0  # info from file

    def get_population_size(self) -> int:
        return self.population_size

    def get_item(self, item_id: int):
        return self.item_store[item_id]

    def get_max_weight(self):
        return self.max_weight

    def get_max_elements(self):
        return self.max_elements

    def get_mutator(self):
        pass

    def get_selector(self):
        pass

    def get_breeder(self):
        pass

    def get_stop_condition(self, pool_manager: PoolManager):
        return {
            "acceptable solution": AcceptableSolution(pool_manager, self.stop_condition_config),
            "generation count": GenerationCount(pool_manager, self.stop_condition_config),
            "same best fitness": SameFitness(pool_manager, self.stop_condition_config),
            "similar structure": SimilarStructure(pool_manager, self.stop_condition_config),
            "time": TimeBased(pool_manager, self.stop_condition_config)
        }[self.stop_condition.lower()]
