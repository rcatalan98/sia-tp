import json

from models.Config import Config

if __name__ == '__main__':
    config_file = open('config.json', 'r')
    config_data = json.load(config_file)
    config = Config(**config_data)
    print(config)


