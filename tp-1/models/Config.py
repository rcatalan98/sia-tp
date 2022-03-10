class Config:
    def __init__(self, algorithm: str, heuristics: str):
        self.algorithm = algorithm
        self.heuristics = heuristics
        self.dic_algorithms = {}
        # TODO load algorithms to the dictionary

    def get_algorithm(self):  # TODO return algorithm with corresponding heuristics
        return self.dic_algorithms[self.algorithm]

    def __str__(self) -> str:
        return f'algorithm: {self.algorithm}\nheuristics: {self.heuristics}'
