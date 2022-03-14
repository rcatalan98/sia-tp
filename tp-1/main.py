import json
import sys

from models.Config import Config
from models.Node import Node
from models.Solution import Solution
from models.State import State
from search_methods.BPA import BPA
from time import perf_counter

if __name__ == '__main__':
    if len(sys.argv) < 2 :
        raise Exception("Invalid parameters. Missing config")

    config_file = open(sys.argv[1], 'r')
    config_data = json.load(config_file)
    config = Config(**config_data)
    algo = config.get_algorithm()

    print("Running algorithm")
    start_time = perf_counter()
    result: Solution = algo.search(Node.root(config.discs))
    end_time = perf_counter()

    result.set_run_time(end_time-start_time)

    if config.print_to_console():
        print(result)
    else:
        print(f"Algorithm finished, open {config.print_to} for the results")
        with open(config.print_to, "w") as text_file:
            text_file.write(str(result))



