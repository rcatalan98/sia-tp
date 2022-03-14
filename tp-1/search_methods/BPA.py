from typing import Tuple, List, Set

from models.Node import Node
from search_methods.Base import Base

class BPA(Base):

    # Para BPA, no hace falta reordenar los nodos, ya que siempre va a usarlos en el orden que entraron
    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        return None
