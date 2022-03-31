from typing import List

from Bag import Bag


class BaseSelection:
    def select(self, population: List[Bag], population_size: int) -> List[Bag]:
        pass
