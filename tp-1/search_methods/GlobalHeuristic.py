from models import Node, Solution
from search_methods.Base import Base
from heuristics.Base import Base as Heuristic


class GlobalHeuristic(Base):

    def __init__(self, heuristic: Heuristic):
        self.heuristic = heuristic

    def search(self, root: Node) -> Solution:
        return super().search(root)
