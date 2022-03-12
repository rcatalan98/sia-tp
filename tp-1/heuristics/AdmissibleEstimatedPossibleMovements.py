from copy import deepcopy

from heuristics.Base import Base
from models import State


class AdmissibleEstimatedPossibleMovements(Base):
    def get_value(self, state: State) -> int:
        s = deepcopy(state)

        top = len(s.first_tower) + len(s.second_tower) + len(s.third_tower)

        while len(s.third_tower) != 0 and s.third_tower[0] == top:
            s.third_tower.pop(0)
            top -= 1

        return 2**(len(s.first_tower) + len(s.second_tower) + len(s.third_tower)-1)-1