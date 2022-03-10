from models.State import State
from typing import List
from copy import deepcopy


class Node:
    def __init__(self, parent, state: State):
        self.parent = parent
        self.state = state
        self.children = []

    def get_children(self) -> List:
        current_state: State = deepcopy(self.state)

        # First Tower Swap
        if len(current_state.first_tower) != 0:
            disc: int = current_state.first_tower.pop()
            other_state = deepcopy(current_state)

            current_state.second_tower.append(disc)
            self.children.append(Node(self, current_state))

            other_state.third_tower.append(disc)
            self.children.append(Node(self, other_state))

        # Second tower swap
        current_state = deepcopy(self.state)
        if len(current_state.second_tower) != 0:
            disc = current_state.second_tower.pop()
            other_state = deepcopy(current_state)

            current_state.first_tower.append(disc)
            self.children.append(Node(self, current_state))

            other_state.third_tower.append(disc)
            self.children.append(Node(self, other_state))

        # Third tower swap
        current_state = deepcopy(self.state)
        if len(current_state.third_tower) != 0:
            disc = current_state.third_tower.pop()
            other_state: State = deepcopy(current_state)

            current_state.first_tower.append(disc)
            self.children.append(Node(self, current_state))

            other_state.second_tower.append(disc)
            self.children.append(Node(self, other_state))

        # Filter only the valid child nodes (hanoi rules and our definitions)
        self.children = list(filter(lambda x: x.state.is_valid(), self.children))

        return self.children

    def __str__(self) -> str:
        return f"Node with state: {self.state}"

    def __eq__(self, other):
        return self.state == other.state

    @classmethod
    def root(cls):
        state = State()
        state.first_tower = [7, 6, 5, 4, 3, 2, 1]
        return Node(None, state)
