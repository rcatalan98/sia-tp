from models import State
from heuristics import Base as Heuristic

class Base:

    def get_value(self, state: State) -> int:
        raise "Method Not Implemented"
