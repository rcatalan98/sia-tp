from typing import Tuple, List

from Bag import Bag
from Breeding.BaseBreeder import BaseBreeder
import random


class UniformBreeder(BaseBreeder):
    def breed(self, first: Bag, second: Bag) -> Tuple[Bag, Bag]:

        l1: List[bool] = []
        l2: List[bool] = []

        for i in range(0, first.elements()):
            if random.uniform(0, 1) <= 0.5:
                l1 += first.items[i:i + 1]
                l2 += second.items[i:i + 1]
            else:
                l1 += second.items[i:i + 1]
                l2 += first.items[i:i + 1]

        return Bag(l1, first.config), Bag(l2, first.config)
