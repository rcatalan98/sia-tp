from models import Node, Solution
from search_methods.Base import Base
from heuristics.Base import Base as Heuristic


class LocalHeuristic(Base):

    def __init__(self, config, heuristic: Heuristic):
        super().__init__(config)
        self.heuristic = heuristic

    def search(self, root: Node) -> Solution:
        return super().search(root)
