from typing import List, Tuple, Set

from models.Node import Node
from models.Solution import Solution
from models.State import State
from search_methods.Base import Base


class NonInformedMethod(Base):  # FIXME: Me parece que se podria unificar esta clase con Base

    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        raise "Not Implemented"

    def search(self, root: Node) -> Solution:
        # It's a tuple that stores the node and the depth
        frontier_nodes: List[Tuple[int, Node]] = list([(0, root)])
        explored_nodes: int = 0
        known_states: Set[State] = set()
        max_depth: int = 0

        while len(frontier_nodes) != 0:
            element = frontier_nodes.pop(0)
            depth = element[0]
            node = element[1]
            max_depth = max(max_depth, depth)
            explored_nodes += 1

            # See if it is the goal
            if node.state.is_solved():
                return Solution(self.config, True, depth, node.get_cost(), explored_nodes, len(frontier_nodes), node.get_moves_until_here())

            # Keep going
            children: List[Node] = node.get_children()
            known_states.add(node.state)

            nodes_to_add = [n for n in children if n.state not in known_states]

            known_states.union([n.state for n in children])
            frontier_nodes.extend([(depth + 1, n) for n in nodes_to_add])
            self.sort_nodes(frontier_nodes)

        return Solution(self.config, False, max_depth, float("inf"), explored_nodes, len(frontier_nodes), [])


