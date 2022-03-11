from models import Node, Solution
from models.Config import Config
from search_methods.Base import Base


class BPPV(Base):

    def search(self, root: Node) -> Solution:
        return super().search(root)

    # Para decidir si tengo que expandir un nodo, tengo que ver su estado y profundidad. Si ya habia expandido un nodo
    # con ese estado, pero a una profundidad mas grande, entonces tengo que expandir a este.