from models import Node, Solution
from search_methods.Base import Base


class BPP(Base):
    def search(self, root: Node) -> Solution:
        return super().search(root)