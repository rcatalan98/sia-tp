from models.Node import Node
from search_methods.Base import Base
from heuristics.Base import Base as Heuristic
from typing import Tuple, List, Set


class GlobalHeuristic(Base):

    def __init__(self, config, heuristic):
        super().__init__(config)
        self.heuristic = heuristic

    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        # Reorder F according to heuristic value
        frontier_nodes.sort(key=self.sort_by_h)

    def sort_by_h(self, n: Tuple[int, Node]):
        return self.heuristic.get_value(n[1].state)
