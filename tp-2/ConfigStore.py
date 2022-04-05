from __future__ import annotations

from typing import Dict

from Breeding.MultipleBreeder import MultipleBreeder
from Breeding.SimpleBreeder import SimpleBreeder
from Breeding.UniformBreeder import UniformBreeder
from Item import Item
from Selection.BoltzmannSelection import BoltzmannSelection
from Selection.EliteSelection import EliteSelection
from Selection.RankSelection import RankSelection
from Selection.RouletteSelection import RouletteSelection
from Selection.TournamentSelection import TournamentSelection
from Selection.TruncatedSelection import TruncatedSelection
from StopCondition.AcceptableSolution import *
from StopCondition.GenerationCount import *
from StopCondition.SameFitness import *
from StopCondition.SimilarStructure import *
from StopCondition.TimeBased import *


class ConfigStore:
    breeding_algorithms = {}
    selection_algorithms = {}

    def __init__(
            self,
            breeding: str, breeding_arguments: Dict[str, float | int],
            selection: str, selection_arguments: Dict[str, float | int],
            stop_condition: str, stop_condition_config: Dict[str, int | float],
            population_size: int, max_weight: int, max_elements: int, mutation_rate: float,
            items: List[Item]
    ):
        self.stop_condition: str = stop_condition
        self.stop_condition_config: Dict[str, int | float] = stop_condition_config

        self.breeder: str = breeding
        self.breeding_arguments: Dict[str, int | float] = breeding_arguments

        self.selection: str = selection
        self.selection_arguments: Dict[str, float | int] = selection_arguments

        self.max_weight: int = max_weight  # info from file
        self.max_elements: int = max_elements  # info from file
        self.population_size: int = population_size  # info from file
        self.mutation_rate: float = mutation_rate

        self.item_store: List[Item] = items  # info from file

    def get_population_size(self) -> int:
        return self.population_size

    def get_item(self, item_id: int):
        return self.item_store[item_id]

    def get_max_weight(self):
        return self.max_weight

    def get_max_elements(self):
        return self.max_elements

    def get_selector(self):
        return {
            'EliteSelection': lambda: EliteSelection(),
            'RankSelection': lambda: RankSelection(),
            'RouletteSelection': lambda: RouletteSelection(),
            'TournamentSelection': lambda: TournamentSelection(**self.selection_arguments),
            'TruncatedSelection': lambda: TruncatedSelection(**self.selection_arguments),
            'BoltzmannSelection': lambda: BoltzmannSelection(**self.selection_arguments)
        }[self.selection]()

    def get_breeder(self):
        return {
            'SimpleBreeder': lambda: SimpleBreeder(),
            'MultipleBreeder': lambda: MultipleBreeder(**self.breeding_arguments),
            'UniformBreeder': lambda: UniformBreeder()
        }[self.breeder]()

    def get_stop_condition(self, pool_manager: PoolManager):
        return {
            "acceptable solution": lambda: AcceptableSolution(pool_manager, **self.stop_condition_config),
            "generation count": lambda: GenerationCount(pool_manager, **self.stop_condition_config),
            "same best fitness": lambda: SameFitness(pool_manager, **self.stop_condition_config),
            "similar structure": lambda: SimilarStructure(pool_manager, **self.stop_condition_config),
            "time": lambda: TimeBased(pool_manager, **self.stop_condition_config)
        }[self.stop_condition.lower()]()
