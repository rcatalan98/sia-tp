from models import Node, Solution
from search_methods.Base import Base
from heuristics.Base import Base as Heuristic
from typing import Tuple, List, Set


class AStar(Base):

    def __init__(self, heuristic):
        self.heuristic = Heuristic(heuristic)  # FIXME: What else?

    def search(self, root: Node) -> Solution:
        frontier_nodes: List[Tuple[int, Node]] = list([(0, root)])
        explored_nodes: Set[Node] = set()  # FIXME: Check if known_states is also needed
        # TODO: solution = Solution(...)

        while frontier_nodes:
            element = frontier_nodes.pop(0)
            depth = element[0]
            node = element[1]

            if node.state.is_solved():
                return node  # TODO return solution

            explored_nodes.add(node)
            children: List[Node] = node.get_children()
            frontier_nodes.extend(list(map(lambda x: (depth + 1, x), children)))

            # Reorder F according to f(n) value
            frontier_nodes.sort(key=self.reorder_by_fn)

        return False  # TODO return solution

    def reorder_by_fn(self, n: Tuple[int, Node]):
        return n[0] + self.heuristic.h(n[1])  # g(n) + h(n.s)
