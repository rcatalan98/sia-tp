import json

from models.Config import Config
from models.Node import Node
from models.Solution import Solution
from models.State import State
from search_methods.BPA import BPA
from time import perf_counter

if __name__ == '__main__':
    config_file = open('config.json', 'r')
    config_data = json.load(config_file)
    config = Config(**config_data)
    algo = config.get_algorithm()

    start_time = perf_counter()
    result: Solution = algo.search(Node.root(config.discs))
    end_time = perf_counter()

    result.set_run_time(end_time-start_time)
    print(result)


