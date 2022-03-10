from models import State


class Base:

    def get_value(self, state: State) -> int:
        raise "Method Not Implemented"
