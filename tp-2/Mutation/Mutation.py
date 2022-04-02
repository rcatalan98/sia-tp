from typing import List

from Bag import Bag
import random


class Mutation:

    def __init__(self, p: float):
        self.p: float = p

    def mutate_gen(self, gen: bool):
        return gen if self.p > random.uniform(0, 1) else not gen

    def mutate(self, subject: Bag) -> Bag:
        return Bag([self.mutate_gen(item) for item in subject.items], subject.config)


