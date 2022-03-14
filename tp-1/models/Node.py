from models.State import State
from typing import List
from copy import deepcopy


class Node:
    def __init__(self, parent, state: State):
        self.parent = parent
        self.state = state
        self.children = []

    def get_cost(self):
        if self.parent:
            return self.parent.get_cost() + 1
        else:
            return 0

    def get_moves_until_here(self):
        if self.parent:
            return self.parent.get_moves_until_here() + [self]
        else:
            return [self]

    def get_children(self) -> List:
        if len(self.children) != 0:
            return self.children

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

    def __gt__(self, other):
        return self.state > other.state

    def __ge__(self, other):
        return self.state >= other.state


    def __lt__(self, other):
        return self.state < other.state

    def __le__(self, other):
        return self.state <= other.state


    @classmethod
    def root(cls, discs: int):
        state = State()
        state.first_tower = [i for i in range(1,1+discs)]
        state.first_tower.sort(reverse=True)
        return Node(None, state)
