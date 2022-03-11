from models import Node, Config
from search_methods.NonInformedMethod import NonInformedMethod
from heuristics.Base import Base as Heuristic
from typing import Tuple, List


class AStar(NonInformedMethod):

    def __init__(self, config: Config, heuristic):
        super().__init__(config)
        self.heuristic = Heuristic(heuristic)  # FIXME: What else?

    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        # Reorder F according to f(n) value
        frontier_nodes.sort(key=self.sort_by_fn)

    def sort_by_fn(self, n: Tuple[int, Node]):
        return n[0] + self.heuristic.h(n[1].state)  # g(n) + h(n.s)
        # TODO: Heuristic.h(state) for each heuristic
