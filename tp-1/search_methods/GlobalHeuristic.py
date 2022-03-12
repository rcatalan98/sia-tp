from models.Node import Node
from search_methods.NonInformedMethod import NonInformedMethod
from heuristics.Base import Base as Heuristic
from typing import Tuple, List, Set


class GlobalHeuristic(NonInformedMethod):

    def __init__(self, config, heuristic: Heuristic):
        super().__init__(config)
        self.heuristic = Heuristic(heuristic)  # FIXME: What else?

    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        # Reorder F according to heuristic value
        frontier_nodes.sort(key=self.sort_by_h)

    def sort_by_h(self, n: Tuple[int, Node]):
        return self.heuristic.get_value(n[1].state)  # TODO: Heuristic.h(state) for each heuristic
