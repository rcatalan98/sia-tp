import json
import sys
from time import perf_counter
from typing import List

from ConfigStore import ConfigStore
from PoolManager import PoolManager
from Bag import Bag
from Item import Item

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception("Invalid parameters. Missing config")

    print("Loading configuration file and items...")

    with open(sys.argv[2], 'r') as items_file:
        lines = items_file.readlines()

    first_line = lines.pop().split(" ")
    max_elements = int(first_line[0])
    max_weight = int(first_line[1])

    items = []
    for line in lines:
        info = lines.pop().split(" ")
        items.append(Item(int(info[0]), int(info[1])))

    config_file = open(sys.argv[1], 'r')
    config_data = json.load(config_file)
    config = ConfigStore(max_weight=max_weight, max_elements=max_elements, items=items, **config_data)

    print("Running...")
    start_time = perf_counter()

    pool_manager = PoolManager(config)  # creates the initial population, called zero generation
    all_generations: List[List[Bag]] = [pool_manager.generation]

    while not pool_manager.has_reached_stop_condition():
        next_gen: List[Bag] = pool_manager.get_new_generation()
        all_generations += next_gen

    end_time = perf_counter()

    # TODO: print results
