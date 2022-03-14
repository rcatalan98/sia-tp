from models import State


class Base:

    def __init__(self, heuristic):  # FIXME: heuristic de que tipo es? String, o no?
        self.h = heuristic

    def get_value(self, state: State) -> int:
        raise "Method Not Implemented"
