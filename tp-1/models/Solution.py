from typing import List
from models import Config


class Solution:
    run_time = None

    def __init__(self, config: Config, success: bool, depth: int, cost: int, n_expanded_nodes: int,
                 n_frontier_nodes: int, states: List):
        self.states = states
        self.n_frontier_nodes = n_frontier_nodes
        self.n_expanded_nodes = n_expanded_nodes
        self.cost = cost
        self.depth = depth
        self.success = success
        self.config = config

    def __str__(self) -> str:
        return "solution"

    def set_run_time(self, run_time: int):
        self.run_time = run_time
