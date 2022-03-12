from heuristics.Base import Base
from models import State


class DiscsOnTheLastTower(Base):
    def get_value(self, state: State) -> int:
        return 7 - len(state.third_tower)
