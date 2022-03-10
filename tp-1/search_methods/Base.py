from models import Solution, Node


class Base:

    def search(self, root: Node) -> Solution:
        raise "Method not Implemented"
