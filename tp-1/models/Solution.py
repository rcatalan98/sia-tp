
from typing import List
from models import State
from models import Config


class Solution:
    def __init__(self, config: Config, success: bool, depth: int, cost: int, n_expanded_nodes: int,
                 n_frontier_nodes: int, states: List, time: int):
        self.states = states
        self.n_frontier_nodes = n_frontier_nodes
        self.n_expanded_nodes = n_expanded_nodes
        self.cost = cost
        self.depth = depth
        self.time = time
        self.success = success
        self.config = config

    def __str__(self) -> str:
        return "solution"
