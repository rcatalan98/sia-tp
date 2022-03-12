from typing import List, Set, Tuple

from models import Node
from models.Solution import Solution
from models.State import State
from search_methods.BPP import BPP


class BPPVConfig:
    def __init__(self, max_depth: int, depth_modifier: int):
        self.max_depth = max_depth
        self.depth_modifier = depth_modifier


class BPPV(BPP):
    def __init__(self, config):
        super().__init__(config)
        self.known_states: Set[Tuple[int, State]] = set()

        if config.BPPV_config is None:
            raise "Invalid parameters: BPPV config missing"

        self.max_depth = config.BPPV_config['max_depth']
        self.depth_modifier = config.BPPV_config['depth_modifier']

    def search(self, root: Node) -> Solution:
        has_finished: bool = False
        has_found_one_solution: bool = False
        last_good_solution = Solution(self.config, False, 0, float("inf"), 0, 0, [])

        while not has_finished and self.max_depth > 1:
            print(f"probando con profundidad {self.max_depth}")
            result = self.search_until_depth(root, self.max_depth)

            if result.success:
                has_found_one_solution = True
                last_good_solution = result
                self.max_depth -= int(self.max_depth * self.depth_modifier)
            else:
                if has_found_one_solution:
                    has_finished = True
                else:
                    self.max_depth += int(self.max_depth * self.depth_modifier)

        return last_good_solution


    def search_until_depth(self,root: Node, max_depth: int) -> Solution:
        # It's a tuple that stores the node and the depth
        frontier_nodes: List[Tuple[int, Node]] = list([(0, root)])
        explored_nodes: List[Node] = list()


        while len(frontier_nodes) != 0:
            element = frontier_nodes.pop(0)
            depth = element[0]
            node = element[1]

            # See if it is the goal
            if node.state.is_solved():
                return Solution(self.config, True, depth, node.get_cost(), len(explored_nodes), len(frontier_nodes), node.get_moves_until_here())

            # See if it exceeds the max depth
            if depth >= max_depth:
                continue

            # Keep going
            children: List[Node] = node.get_children()
            self.known_states.add((depth, node.state))
            explored_nodes.append(node)

            nodes_to_add = [ (depth + 1, c) for c in children if not any(c.state == n[1] and depth + 1 > n[0] for n in self.known_states)]

            self.known_states.union([(n[0], n[1].state) for n in nodes_to_add])
            frontier_nodes.extend(nodes_to_add)
            self.sort_nodes(frontier_nodes)

        return Solution(self.config, False, depth, float("inf"), len(explored_nodes), len(frontier_nodes), [])


    # Para decidir si tengo que expandir un nodo, tengo que ver su estado y profundidad. Si ya habia expandido un nodo
    # con ese estado, pero a una profundidad mas grande, entonces tengo que expandir a este.



