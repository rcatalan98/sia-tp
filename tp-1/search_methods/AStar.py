from models.Node import Node
from search_methods.Base import Base
from heuristics.Base import Base as Heuristic
from typing import Tuple, List


class AStar(Base):  # FIXME: Es informado y extiende a Base, raro

    def __init__(self, config, heuristic):
        super().__init__(config)
        self.heuristic = Heuristic(heuristic)  # FIXME: What else?

    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        # Reorder F according to f(n) value
        frontier_nodes.sort(key=self.sort_by_fn)

    def sort_by_fn(self, n: Tuple[int, Node]):
        return n[0] + self.heuristic.get_value(n[1].state)  # g(n) + h(n.s)
