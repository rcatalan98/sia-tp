from random import randint

# Function for couple selection

# Basic selection for even number of population
import random

from Bag import Bag


def chunks(l, n):
    """Yield n number of striped chunks from l."""
    for i in range(0, n):
        yield l[i::n]
    # ToDo check when len(l) is odd


# Functions for breeding
def simple_breeding(p1: Bag, p2: Bag):
    # number of elements taken from the parent 1
    rand = randint(1, p1.config.max_elements - 1)

    sub_list_p1 = p1.items[:rand]
    sub_list_p2 = p2.items[rand + 1:]
    c1 = Bag(sub_list_p1 + sub_list_p2, p1.config)

    sub_list_p1 = p1.items[rand + 1:]
    sub_list_p2 = p2.items[:rand]
    c2 = Bag(sub_list_p2 + sub_list_p1, p1.config)

    return c1, c2
