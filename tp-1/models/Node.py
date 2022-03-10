from models import State
from typing import List


class Node:
    def __init__(self, parent, state: State):
        self.parent = parent
        self.state = state
        self.children = []

    def get_children(self) -> List:
        return self.children  # TODO children logic.

    def __str__(self) -> str:  # TODO logic
        return "chau"
