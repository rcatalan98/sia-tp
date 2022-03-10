import json
from models.Config import Config
from models.Node import Node
from models.State import State
from search_methods.BPA import BPA

if __name__ == '__main__':
    config_file = open('config.json', 'r')
    config_data = json.load(config_file)
    config = Config(**config_data)
    algo = config.get_algorithm()
    print(algo)

    result = BPA().search(Node.root())

    print(result)


