# Subject
from typing import List
import random
from frozenlist import FrozenList



class Bag:
    def __init__(self, items: List[bool], config):
        self.items: FrozenList = FrozenList(items)
        self.items.freeze()
        self.config = config
        self.id = ''.join([str(int(i)) for i in self.items])
        self.weight = sum(
            [self.config.get_item(index).weight for index, has_item in enumerate(self.items) if has_item])
        self.elements = len([has_item for has_item in self.items if has_item])
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
            return sum([self.config.get_item(index).benefit for index, has_item in enumerate(self.items) if has_item])
        else:
            return 0

    def is_valid(self) -> bool:
        return self.weight <= self.config.max_weight and \
               self.elements <= self.config.max_elements

    @staticmethod
    def create_random(config):
        total_items: int = len(config.item_store)


        items: List[bool] = [False] * total_items

        # Elijo la cantidad de elementos que van a estar en la mochila
        elements: int = random.randint(0, config.max_elements)
        # Elijo los elementos que voy a meter en la mochila.
        for i in random.sample(range(0, total_items), elements):
            items[i] = True

        return Bag(items, config)
