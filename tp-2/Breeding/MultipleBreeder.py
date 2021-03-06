import random
from typing import Tuple, List

from Bag import Bag
from Breeding.BaseBreeder import BaseBreeder


class MultipleBreederConfig:

    def __init__(self, crossing_points: int) -> None:
        self.crossing_points = crossing_points


class MultipleBreeder(BaseBreeder):
    def __init__(self, crossing_points: int):
        self.points = crossing_points

    def breed(self, first: Bag, second: Bag) -> Tuple[Bag, Bag]:
        # Elije multiples puntos entre 0 y len(first)
        crossing_points: List[int] = sorted(
            [0, len(first)] + random.sample(range(1, len(first)), self.points))

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
