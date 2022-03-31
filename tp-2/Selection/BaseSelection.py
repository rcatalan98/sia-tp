from typing import List

from Bag import Bag


class BaseSelection:
    def select(self, population: List[Bag]) -> List[Bag]:
        pass
