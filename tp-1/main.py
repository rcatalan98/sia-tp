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
    print(config)
    algo = config.get_algorithm()
    print(algo)

    start_time = perf_counter()
    result = algo.search(Node.root())
    end_time = perf_counter()

    print(f'Time running the algorithm: {end_time-start_time}s')
    print(result)


