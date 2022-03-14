from time import perf_counter
from typing import List, Set, Tuple, Dict

from models.Node import Node
from models.Solution import Solution
from models.State import State
from search_methods.BPP import BPP
from collections import defaultdict


class BPPVConfig:
    def __init__(self, max_depth: int, depth_modifier: int):
        self.max_depth = max_depth
        self.depth_modifier = depth_modifier


class BPPV(BPP):
    def __init__(self, config):
        super().__init__(config)
        self.known_states: Dict[State,Set[int]] = defaultdict(lambda: set(),{})

        if config.BPPV_config is None:
            raise Exception("Invalid parameters: BPPV config missing")

        self.max_depth = config.BPPV_config['max_depth']
        self.depth_modifier = config.BPPV_config['depth_modifier']

    def search(self, root: Node) -> Solution:
        has_finished: bool = False
        has_found_one_solution: bool = False
        last_good_solution = Solution.NoSolution(self.config, 0, 0, 0)
        self.known_states[root.state] = set([0])
        self.next_frontier_nodes = []

        frontier_nodes :List[Tuple[int, Node]] = [(0,root)]

        while not has_finished and self.max_depth > 1:
            # print(f"Using max depth: {self.max_depth}")
            # start_time = perf_counter()
            result = self.search_until_depth(frontier_nodes, self.max_depth,last_good_solution.n_expanded_nodes)
            # end_time = perf_counter()
            # print(end_time - start_time)

            if result.success:
                has_found_one_solution = True
                last_good_solution = result
                self.max_depth = result.cost - 1
                frontier_nodes = [(d,n) for (d,n) in frontier_nodes if d <=self.max_depth ]
            else:
                if has_found_one_solution:
                    has_finished = True
                else:
                    frontier_nodes = self.next_frontier_nodes
                    self.next_frontier_nodes = []
                    self.max_depth += int(self.max_depth * self.depth_modifier)

        return last_good_solution

    def search_until_depth(self, frontier_nodes: List[Tuple[int, Node]], max_depth: int, previous_explored_nodes: int = 0) -> Solution:
        # It's a tuple that stores the node and the depth
        # frontier_nodes: List[Tuple[int, Node]] = list([(0, root)])
        explored_nodes: int = previous_explored_nodes

        while len(frontier_nodes) != 0:
            (depth, node) = frontier_nodes.pop(0)

            # See if it exceeds the max depth
            if depth >= max_depth:
                self.next_frontier_nodes +=[(depth,node)]
                continue

            explored_nodes += 1


            # See if it is the goal
            if node.state.is_solved():
                return Solution(self.config, True, depth, node.get_cost(), explored_nodes, len(frontier_nodes),
                                node.get_moves_until_here())

            # Keep going
            children: List[Node] = node.get_children()
            child_depth: int = depth + 1

            nodes_to_add = [(child_depth, c)
                            for c in children if
                            c.state not in self.known_states or child_depth < min(self.known_states[c.state])
                            ]

            frontier_nodes += nodes_to_add
            for (d,n) in nodes_to_add:
                self.known_states[n.state] |= set([d])

            self.sort_nodes(frontier_nodes)

        return Solution.NoSolution(self.config, max_depth, explored_nodes, len(frontier_nodes))

