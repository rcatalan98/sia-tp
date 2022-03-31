from Bag import Bag
import random


class Mutation:

    def mutate(self, subject: Bag, p: float) -> Bag:
        mutated_bag: Bag = Bag()
        for i in range(0, len(subject.items)):
            item = subject.items[i]
            u: float = random.uniform(0, 1)
            mutated_bag.items[i] = not item if p < u else item
        return mutated_bag


