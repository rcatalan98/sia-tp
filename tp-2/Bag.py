# Subject
from typing import List

from ConfigStore import ConfigStore


class Bag:
    def __init__(self, items: List[bool], config: ConfigStore):
        self.items = items
        self.config = config

    def id(self) -> str:
        return str([[i for i in self.items]])

    def __hash__(self) -> int:
        return hash(self.id())

    def __eq__(self, other):
        return self.id() == other.id()

    def __str__(self) -> str:
        return self.id()

    def fitness(self) -> int:
        return sum([[self.config.get_item(index).benefit for index, has_item in enumerate(self.items) if has_item]])

    def weight(self) -> int:
        return sum([[self.config.get_item(index).weight for index, has_item in enumerate(self.items) if has_item]])

    def elements(self) -> int:
        return len([[has_item for has_item in self.items if has_item]])

    def is_valid(self) -> bool:
        return self.weight() <= self.config.max_weight and \
                self.elements() <= self.config.max_elements
