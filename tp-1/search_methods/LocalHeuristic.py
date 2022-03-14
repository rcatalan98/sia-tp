from typing import List, Tuple, Set

from models.Node import Node
from models.Solution import Solution
from search_methods.Base import Base
from heuristics.Base import Base as Heuristic


class LocalHeuristic(Base):

    def __init__(self, config, heuristic):
        super().__init__(config)
        self.heuristic = Heuristic(heuristic)  # FIXME: What else?

    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        pass

    def search(self, root: Node) -> Solution:
        return self.search_aux(list([(0, root)]), 1, 0, set())

    def search_aux(self, list1: List[Tuple[int, Node]], frontier_nodes_qty: int, explored_nodes_qty: int, known_states):
        while len(list1) > 0:
            # frontier_nodes_qty --
            # explored_nodes_qty ++
            e = self.min_element(list1)
            depth = e[0]
            node = e[1]

            if node.state.is_solved():
                return Solution(self.config, True, depth, node.get_cost(), frontier_nodes_qty - 1,
                                explored_nodes_qty + 1, node.get_moves_until_here())

            children: List[Node] = node.get_children()
            known_states.add(node.state)

            nodes_to_add = filter(
                lambda n: n.state not in known_states,
                children
            )

            known_states.union(map(lambda s: s.state, children))
            l_ancestors = list(map(lambda x: (depth + 1, x), nodes_to_add))
            # frontier_nodes_qty += len(l_ancestors)

            possible_sol = self.search_aux(l_ancestors, frontier_nodes_qty - 1 + len(l_ancestors),
                                           explored_nodes_qty + 1, known_states)
            if possible_sol.success:
                return possible_sol

            list1.remove(e)

        return Solution(self.config, False, -1, float("inf"), explored_nodes_qty, frontier_nodes_qty, [])

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
