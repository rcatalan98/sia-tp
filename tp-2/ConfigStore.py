from __future__ import annotations

from typing import List, Dict

from Item import Item
from StopCondition.AcceptableSolution import *
from StopCondition.GenerationCount import *
from StopCondition.SameFitness import *
from StopCondition.SimilarStructure import *
from StopCondition.TimeBased import *
from Breeding.MultipleBreeder import MultipleBreeder
from Breeding.SimpleBreeder import SimpleBreeder
from Breeding.UniformBreeder import UniformBreeder
from Selection.EliteSelection import EliteSelection
from Selection.RankSelection import RankSelection
from Selection.RouletteSelection import RouletteSelection
from Selection.TournamentSelection import TournamentSelection
from Selection.TruncatedSelection import TruncatedSelection


class ConfigStore:
    breeding_algorithms = {}
    selection_algorithms = {}

    def __init__(self, breeding: str, selection: str, selection_arguments: Dict[str, str], population_size: int, max_weight: int, max_elements: int,
                 items: List[Item], stop_condition: str):
        # load file
        self.stop_condition_config: Dict[str,int|float] = None
        self.load_selection_algorithms()
        self.load_breeding_algorithms()

        self.breeding = self.breeding_algorithms[breeding]
        self.selection = self.selection_algorithms[selection]
        self.selection_arguments = selection_arguments
        self.stop_condition: str = stop_condition
        self.max_weight = max_weight  # info from file
        self.max_elements = max_elements  # info from file
        self.population_size = population_size  # info from file
        self.item_store: List[Item] = items  # info from file

    def load_breeding_algorithms(self):
        # loading breeding algorithms
        self.breeding_algorithms['SimpleBreeder'] = lambda x: SimpleBreeder()
        self.breeding_algorithms['MultipleBreeder'] = lambda x: MultipleBreeder(self, x)
        self.breeding_algorithms['UniformBreeder'] = lambda x: UniformBreeder()

    def load_selection_algorithms(self):
        self.selection_algorithms['EliteSelection'] = lambda x: EliteSelection()
        self.selection_algorithms['RankSelection'] = lambda x: RankSelection()
        self.selection_algorithms['RouletteSelection'] = lambda x: RouletteSelection()
        self.selection_algorithms['TournamentSelection'] = lambda x: TournamentSelection()
        self.selection_algorithms['TruncatedSelection'] = lambda x: TruncatedSelection()

    def get_population_size(self) -> int:
        return self.population_size

    def get_item(self, item_id: int):
        return self.item_store[item_id]

    def get_max_weight(self):
        return self.max_weight

    def get_max_elements(self):
        return self.max_elements

    def get_selector(self):
        return self.selection

    def get_breeder(self):
        return self.breeding

    def get_stop_condition(self, pool_manager: PoolManager):
        return {
            "acceptable solution": lambda: AcceptableSolution(pool_manager, self.stop_condition_config),
            "generation count": lambda: GenerationCount(pool_manager, self.stop_condition_config),
            "same best fitness": lambda: SameFitness(pool_manager, self.stop_condition_config),
            "similar structure": lambda: SimilarStructure(pool_manager, self.stop_condition_config),
            "time": lambda: TimeBased(pool_manager, self.stop_condition_config)
        }[self.stop_condition.lower()]()
