from typing import List
from models import Config


class Solution:
    run_time = None

    def __init__(self, config: Config, success: bool, depth: int, cost: float, n_expanded_nodes: int,
                 n_frontier_nodes: int, states: List):
        self.states = states
        self.n_frontier_nodes = n_frontier_nodes
        self.n_expanded_nodes = n_expanded_nodes
        self.cost = cost
        self.depth = depth
        self.success = success
        self.config = config

    def __str__(self):
        if self.success:
            states = "".join([f"{n.state}\n" for n in self.states])
            if self.run_time is None:
                raise f'Solution must have an end time'
            return (f"Found solution in {self.run_time} seconds!"
                    "\n\n"
                    "It has: \n"
                    f"\t{self.n_frontier_nodes} frontier nodes\n"
                    f"\t{self.n_expanded_nodes} expanded nodes\n"
                    f"\t{self.cost} cost"
                    "\n\n"
                    "The solution is:\n"
                    f"{states}"
                    "\n\n"
                    "The configuration was:"
                    f"{self.config}")
        else:
            return f"The algorithm ran for {self.run_time} seconds but it couldn't find an solution" \
                   f"\n\n" \
                   f"It finished with:" \
                   f"\t{self.n_frontier_nodes} frontier nodes" \
                   f"\t{self.n_expanded_nodes} expanded nodes" \
                   f"\t{self.cost} cost" \
                   f"\n\n" \
                   f"The configuration was:" \
                   f"{self.config}"

    def set_run_time(self, run_time: float):
        self.run_time = run_time
