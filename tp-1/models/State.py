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
        return f"{self.first_tower} {self.second_tower} {self.third_tower}"

    def __gt__(self, other):
        return len(self.first_tower) + 10 * len(self.second_tower) + 100 * len(self.third_tower) > len(other.first_tower) + 10 * len(other.second_tower) + 100 * len(other.third_tower)

    def __ge__(self, other):
        return len(self.first_tower) + 10 * len(self.second_tower) + 100 * len(self.third_tower) >= len(other.first_tower) + 10 * len(other.second_tower) + 100 * len(other.third_tower)

    def __lt__(self, other):
        return len(self.first_tower) + 10 * len(self.second_tower) + 100 * len(self.third_tower) < len(other.first_tower) + 10 * len(other.second_tower) + 100 * len(other.third_tower)

    def __le__(self, other):
        return len(self.first_tower) + 10 * len(self.second_tower) + 100 * len(self.third_tower) <= len(other.first_tower) + 10 * len(other.second_tower) + 100 * len(other.third_tower)
