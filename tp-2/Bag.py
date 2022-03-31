# Subject
from typing import List
import random
from frozenlist import FrozenList
from ConfigStore import ConfigStore


class Bag:
    def __init__(self, items: List[bool], config: ConfigStore):
        self.items: FrozenList = FrozenList(items)
        self.items.freeze()
        self.config = config
        self.id = str(self.items)
        self.weight = sum(
            [[self.config.get_item(index).weight for index, has_item in enumerate(self.items) if has_item]])
        self.elements = len([[has_item for has_item in self.items if has_item]])
        self.fitness = self.calculate_fitness()

    def __hash__(self) -> int:
        return hash(self.items)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self) -> str:
        return self.id

    def __len__(self):
        return len(self.items)

    def calculate_fitness(self):
        if self.is_valid():
            return sum([[self.config.get_item(index).benefit for index, has_item in enumerate(self.items) if has_item]])
        else:
            return 0

    def is_valid(self) -> bool:
        return self.weight <= self.config.max_weight and \
               self.elements <= self.config.max_elements

    @staticmethod
    def create_random(config: ConfigStore):
        total_items: int = len(config.itemStore)
        items: List[bool] = [random.randint(0, 1) == 0 for i in range(total_items)]
        return Bag(items, config)
