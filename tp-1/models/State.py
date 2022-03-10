class State:
    def __init__(self):
        self.first_tower = []
        self.second_tower = []
        self.third_tower = []
        self.id = hash([self.first_tower, self.second_tower, self.third_tower])

    def is_solved(self) -> bool:  # TODO logic
        return True

    def is_valid(self) -> bool:  # TODO logic
        return False

    def __str__(self) -> str:  # TODO logic
        return "hola"
