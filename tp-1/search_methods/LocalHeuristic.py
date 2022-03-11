from models import Node, Solution
from models.Config import Config
from search_methods.Base import Base
from heuristics.Base import Base as Heuristic


class LocalHeuristic(Base):

    def __init__(self, config: Config, heuristic: Heuristic):
        super().__init__(config)
        self.heuristic = heuristic

    def search(self, root: Node) -> Solution:
        return super().search(root)
