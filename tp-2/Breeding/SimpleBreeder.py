from random import randint
from typing import List, Tuple

from Bag import Bag
from Breeding.BaseBreeder import BaseBreeder
from Breeding.MultipleBreeder import MultipleBreeder


class SimpleBreeder(MultipleBreeder):
    def __init__(self):
        super().__init__(1)


