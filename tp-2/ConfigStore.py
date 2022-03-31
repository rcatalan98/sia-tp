from typing import List

from Item import Item


class ConfigStore:
    def __init__(self, file: str):
        # load file
        self.itemStore: List[Item] = []
        self.max_weight = 0  # info from file
        self.max_elements = 0  # info from file
        self.population_size = 0    # info from file

    def get_population_size(self) -> int:
        return self.population_size
    def get_item(self, item_id: int):
        return self.itemStore[item_id]

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
