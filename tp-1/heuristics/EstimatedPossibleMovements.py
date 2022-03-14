from copy import deepcopy

from heuristics.Base import Base
from models import State


class EstimatedPossibleMovements(Base):
    def get_value(self, state: State) -> int:
        s = deepcopy(state)

        top = len(s.first_tower) + len(s.second_tower) + len(s.third_tower)

        while len(s.third_tower) != 0 and s.third_tower[0] == top:
            s.third_tower.pop(0)
            top -= 1
            
        num = 0
        for i in s.first_tower:
            num += 3 ** i
        for i in s.second_tower:
            num += 3 ** i
        for i in s.third_tower:
            num += 3 ** i
        return num