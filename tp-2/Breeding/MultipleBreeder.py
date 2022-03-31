import random
from typing import Tuple, List

from Bag import Bag
from Breeding.BaseBreeder import BaseBreeder


class MultipleBreeder(BaseBreeder):
    def __init__(self, k: int):
        self.points = k

    def breed(self, first: Bag, second: Bag) -> Tuple[Bag, Bag]:
        # Elije multiples puntos entre 0 y elements()
        crossing_points: List[int] = sorted(
            [0, first.elements()] + random.sample(range(1, len(first)), self.points))

        l1: List[bool] = []
        l2: List[bool] = []

        for i in range(0, len(crossing_points) - 1):
            if i % 2:
                l1 += first.items[crossing_points[i]:crossing_points[i + 1]]
                l2 += second.items[crossing_points[i]:crossing_points[i + 1]]
            else:
                l1 += second.items[crossing_points[i]:crossing_points[i + 1]]
                l2 += first.items[crossing_points[i]:crossing_points[i + 1]]

        return Bag(l1, first.config), Bag(l2, first.config)
