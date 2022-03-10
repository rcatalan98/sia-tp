from heuristics.Basic import Basic
from search_methods.AStar import AStar
from search_methods.BPA import BPA
from search_methods.BPP import BPP
from search_methods.BPPV import BPPV
from search_methods.GlobalHeuristic import GlobalHeuristic
from search_methods.LocalHeuristic import LocalHeuristic


def load_algorithms(algorithms: {}):
    algorithms['BPA'] = lambda x: BPA
    algorithms['BPP'] = lambda x: BPP
    algorithms['BPPV'] = lambda x: BPPV
    algorithms['AStar'] = lambda x: AStar(x)
    algorithms['GlobalHeuristic'] = lambda x: GlobalHeuristic(x)
    algorithms['LocalHeuristic'] = lambda x: LocalHeuristic(x)


def load_heuristics(h: {}):
    h['Basic'] = Basic()


class Config:
    def __init__(self, algorithm: str, heuristics: str = None):
        self.algorithm = algorithm
        self.heuristics = heuristics
        self.dic_algorithms = {}
        if heuristics is not None:
            self.dic_heuristics = {}
            load_heuristics(self.dic_heuristics)
        load_algorithms(self.dic_algorithms)

    def get_algorithm(self):
        h = self.heuristics if self.heuristics is None else self.dic_heuristics[self.heuristics]
        return self.dic_algorithms[self.algorithm](h)

    def __str__(self) -> str:
        return f'algorithm: {self.algorithm}\nheuristics: {self.heuristics}'
