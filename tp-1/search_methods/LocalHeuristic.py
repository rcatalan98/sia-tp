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
        sys.setrecursionlimit(10 ** 6)

    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        pass

    def search(self, root: Node) -> Solution:
        return self.search_aux(list([(0, root)]), 1, 0, set())

    def search_aux(self, frontier_nodes: List[Tuple[int, Node]], frontier_nodes_qty: int, explored_nodes_qty: int, known_states: Set[State]):
        while len(frontier_nodes) > 0:
            (depth, node) = self.min_element(frontier_nodes)

            if node.state.is_solved():
                return Solution(self.config, True, depth, node.get_cost(), frontier_nodes_qty - 1,
                                explored_nodes_qty + 1, node.get_moves_until_here())

            children: List[Node] = node.get_children()
            known_states.add(node.state)

            nodes_to_add = [n for n in children if n.state not in known_states]

            known_states |= set([n.state for n in nodes_to_add])
            l_ancestors = [(depth + 1, x) for x in nodes_to_add]

            possible_sol = self.search_aux(l_ancestors, frontier_nodes_qty - 1 + len(l_ancestors),
                                           explored_nodes_qty + 1, known_states)
            if possible_sol.success:
                return possible_sol

            frontier_nodes.remove((depth,node))

        return Solution.NoSolution(self.config, 0, explored_nodes_qty, frontier_nodes_qty)

    def min_element(self, list1):
        t = list1[0]
        min1 = t
        min_h = self.h(t[1].state)

        for i in range(len(list1)):
            t = list1[i]
            if self.h(t[1].state) < min_h:
                min1 = t
                min_h = self.h(t[1].state)

        return min1

    def h(self, state):
        return self.heuristic.get_value(state)
