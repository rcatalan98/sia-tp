from models import Solution, Node
from models.Config import Config


class Base:
    def __init__(self, config: Config):
        self.config = config

    def search(self, root: Node) -> Solution:
        raise "Method not Implemented"

    def __str__(self):
        return f'algorithm'
