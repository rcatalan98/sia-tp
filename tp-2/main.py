import json
import os
import sys
from time import perf_counter
from typing import List

from ConfigStore import ConfigStore
from PoolManager import PoolManager
from Bag import Bag
from Item import Item


def load_settings(item_description_filename: str, config_filename: str) -> ConfigStore:
    with open(item_description_filename, 'r') as items_file:
        lines = items_file.readlines()

    # Python loads the lines in the order it reads them, so if you pop directly, it will read the last line
    lines.reverse()

    first_line = lines.pop().split(" ")
    max_elements = int(first_line[0])
    max_weight = int(first_line[1])

    items = []
    for line in lines:
        # There's no need to pop anything at this point. this list is not used anywhere
        info = line.split(" ")
        items.append(Item(int(info[0]), int(info[1])))

    with open(config_filename, 'r') as config_file:
        config_data = json.load(config_file)

    return ConfigStore(max_weight=max_weight, max_elements=max_elements, items=items, **config_data)

def load_multiple_settings(item_description_filename: str, config_directory: str) -> List[ConfigStore]:
    a = [load_settings(item_description_filename,val) for sublist in [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(config_directory)] for val in sublist]

    return a

def run(config: ConfigStore) -> str:
    start_time = perf_counter()

    pool_manager = PoolManager(config)  # creates the initial population, called zero generation
    # TODO: Por que necesitamos guardar todas las generaciones???
    # all_generations: List[List[Bag]] = [pool_manager.generation]


    while not pool_manager.has_reached_stop_condition():
        next_gen: List[Bag] = pool_manager.get_new_generation()
        # print(f"{pool_manager.generation}: {pool_manager.all_fitness[-1]}")

    end_time = perf_counter()
    return f"{config.breeder},{config.breeding_arguments}," \
           f"{config.selection},{config.selection_arguments}," \
           f"{config.stop_condition}, {config.stop_condition_config}," \
           f"{config.population_size},{config.mutation_rate}," \
           f"{end_time-start_time},{pool_manager.all_fitness[-1]},{pool_manager.generation}," \
           f"[{';'.join(str(i) for i in pool_manager.all_fitness)}]"

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception("Invalid parameters. Missing config")

    settings: List[ConfigStore] = []
    runs: int = 1
    if sys.argv[2] == 'multiple':
        settings = load_multiple_settings(sys.argv[1],sys.argv[3])
        if len(sys.argv) == 5:
            runs = int(sys.argv[4])
    else:
        settings.append(load_settings(sys.argv[1],sys.argv[2]))
        if len(sys.argv) == 4:
            runs = int(sys.argv[3])



    report: str = "breeder, breeder args, selector, selector_args," \
                  "stop condition,stop condition args, population size," \
                  "mutation rate, time elapsed, max fitness, max generation," \
                  "fitness per generation\n"

    for config in settings:
        for i in range(runs):
            print(config.stop_condition)
            a = run(config)
            print(a)
            report += f"{a}\n"

    f = open("results.csv",'w')
    f.write(report)
    f.close()

