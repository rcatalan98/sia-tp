import json
from models.Config import Config
from models.Node import Node
from models.State import State

if __name__ == '__main__':
    config_file = open('config.json', 'r')
    config_data = json.load(config_file)
    config = Config(**config_data)
    print(config)

    state: State = State()
    state.first_tower = [3, 2]
    state.second_tower = [1]
    state.third_tower = [4]
    root: Node = Node(None, state)

    children = root.get_children()


