from typing import List, Tuple, Set

from models.Node import Node
from models.Solution import Solution
from models.State import State
from search_methods.Base import Base

import sys


class LocalHeuristic(Base):

    def __init__(self, config, heuristic):
        super().__init__(config)
        self.heuristic = heuristic

    def sort_nodes(self, frontier_nodes: List[Tuple[int, int, Node]]) -> None:
        frontier_nodes.sort(key=lambda n: (n[0], n[1]))

    def search(self, root: Node) -> Solution:
        explored_nodes: int = 0
        # It's a tuple that stores the node, and the depth and the node opening
        frontier_nodes: List[Tuple[int, int, int, Node]] = list([(explored_nodes, 0, 0, root)])
        known_states: Set[State] = set([root.state])
        max_depth: int = 0


        while len(frontier_nodes) != 0:
            (spot, heuristic_value, depth, node) = frontier_nodes.pop(0)
            max_depth = max(max_depth, depth)
            explored_nodes += 1

            # See if it is the goal
            if node.state.is_solved():
                return Solution(self.config, True, depth, node.get_cost(), explored_nodes, len(frontier_nodes),
                                node.get_moves_until_here())

            # Keep going
            children: List[Node] = node.get_children()

            nodes_to_add = [n for n in children if n.state not in known_states]

            known_states |= set([n.state for n in nodes_to_add])

            frontier_nodes.extend([(explored_nodes, self.heuristic.get_value(n.state), depth + 1, n) for n in nodes_to_add])
            self.sort_nodes(frontier_nodes)

        return Solution.NoSolution(self.config, max_depth, explored_nodes, len(frontier_nodes))
