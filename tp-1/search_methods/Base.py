from models import Solution, Node


class Base:
    def __init__(self, config):
        self.config = config

    def search(self, root: Node) -> Solution:
        raise "Method not Implemented"

    def __str__(self):
        return f'algorithm'
