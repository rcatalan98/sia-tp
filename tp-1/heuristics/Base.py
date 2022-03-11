from models import State


# TODO
class Base:

    def __init__(self, heuristic):
        self.h = heuristic

    def get_value(self, state: State) -> int:
        raise "Method Not Implemented"
