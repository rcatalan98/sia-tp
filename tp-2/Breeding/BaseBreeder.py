from typing import Tuple

from Bag import Bag


class BaseBreeder:

    def breed(self, first: Bag, second: Bag) -> Tuple[Bag, Bag]:
        pass
