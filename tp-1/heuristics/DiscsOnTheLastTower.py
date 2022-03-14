from heuristics.Base import Base
from models import State

# ESTA ES LA MEJOR
class DiscsOnTheLastTower(Base):
    def get_value(self, state: State) -> int:
        return 7 - len(state.third_tower)
