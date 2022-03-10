from utils import is_sorted


class State:
    def __init__(self):
        self.first_tower = []
        self.second_tower = []
        self.third_tower = []

    def __hash__(self):
        return hash(f"{self.first_tower} {self.second_tower} {self.third_tower}")

    def __eq__(self, other):
        return hash(self) == hash(other)

    def is_solved(self) -> bool:
        return len(self.first_tower) == 0 and \
               len(self.second_tower) == 0 and \
               is_sorted(self.third_tower)

    def is_valid(self) -> bool:
        return is_sorted(self.first_tower) and \
               is_sorted(self.second_tower) and \
               is_sorted(self.third_tower)

    def __str__(self) -> str:
        return f"first tower: {self.first_tower}\nsecond_tower: {self.second_tower}\nthird_tower: {self.third_tower}"
