from typing import List, Tuple, Set

from models.Node import Node
from search_methods.Base import Base


    # Este tambien esta medio raro
    # Tiene la misma cantidad de nodos expandidos que BPA
    # FIXME: Investigar esto
class BPP(Base):
    def sort_nodes(self, frontier_nodes: List[Tuple[int, Node]]) -> None:
        frontier_nodes.sort(key=lambda n: n[0], reverse=False)
