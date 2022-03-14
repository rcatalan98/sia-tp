from typing import Tuple, List, Set

from models.Node import Node
from search_methods.Base import Base

class BPA(Base):

    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        frontier_nodes.sort(key=lambda n: n[0], reverse=True)
