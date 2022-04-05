import random

from Bag import Bag


class Mutation:

    def __init__(self, mutation_rate: float):
        self.mutation_rate: float = mutation_rate

    def mutate_gen(self, gen: bool):
        return gen if self.mutation_rate > random.uniform(0, 1) else not gen

    def mutate(self, subject: Bag) -> Bag:
        l = []
        for item in subject.items:
            if random.uniform(0, 1) > self.mutation_rate:
                l += [item]
            else:
                l += [not item]

        return Bag(l, subject.config)
