class Node:
    def __init__(self, parent, state):
        self.parent = parent
        self.state = state
        self.children = []

    def get_children(self):
        return self.children  # TODO children logic.

    def __str__(self):  # TODO logic
        return "chau"
