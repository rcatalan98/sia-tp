from typing import Tuple, List, Set

from models import Node, Solution
from search_methods.Base import Base


class BPA(Base):

    def search(self, root: Node) -> Solution:
        # It's a tuple that stores the node and the depth
        frontier_nodes: List[Tuple[int, Node]] = list([(0, root)])
        explored_nodes: List[Node] = list()
        known_states: Set[Node] = set()

        while len(frontier_nodes) != 0:
            element = frontier_nodes.pop(0)
            depth = element[0]
            node = element[1]
            children: List[Node] = node.get_children()
            known_states.add(node.state)
            known_states.union(map(lambda s: s.state,children))

            # See if it is the goal

            if node.state.is_solved():
                return node

            # Keep going
            explored_nodes.append(node)

            nodes_to_add = filter(
                lambda n:  n.state not in known_states,
                children
            )

            frontier_nodes.extend(list(map(lambda x: (depth + 1, x), nodes_to_add)))

        return False
