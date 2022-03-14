from abc import abstractmethod, ABC
from typing import List, Tuple, Set

from models.Solution import Solution
from models.Node import Node
from models.State import State


class Base(ABC):
    def __init__(self, config):
        self.config = config

    @abstractmethod
    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        pass

    def search(self, root: Node) -> Solution:
        # It's a tuple that stores the node and the depth
        frontier_nodes: List[Tuple[int, Node]] = list([(0, root)])
        explored_nodes: int = 0
        known_states: Set[State] = set()
        max_depth: int = 0

        while len(frontier_nodes) != 0:
            (depth, node) = frontier_nodes.pop(0)
            max_depth = max(max_depth, depth)
            explored_nodes += 1

            # See if it is the goal
            if node.state.is_solved():
                return Solution(self.config, True, depth, node.get_cost(), explored_nodes, len(frontier_nodes),
                                node.get_moves_until_here())

            # Keep going
            children: List[Node] = node.get_children()
            known_states.add(node.state)

            nodes_to_add = [n for n in children if n.state not in known_states]

            known_states |= set([n.state for n in nodes_to_add])
            frontier_nodes.extend([(depth + 1, n) for n in nodes_to_add])
            self.sort_nodes(frontier_nodes)

        return Solution.NoSolution(self.config, max_depth, explored_nodes, len(frontier_nodes))
