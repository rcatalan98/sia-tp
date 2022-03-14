from models import Solution, Node


class Base:  # FIXME: Me parece que se podria unificar esta clase con NonInformedMethod
    def __init__(self, config):
        self.config = config

    def search(self, root: Node) -> Solution:
        raise "Method not Implemented"

    def __str__(self):
        return f'algorithm'
