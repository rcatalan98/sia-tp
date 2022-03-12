from heuristics.DiscsOnTheLastTower import DiscsOnTheLastTower
from search_methods.AStar import AStar
from search_methods.BPA import BPA
from search_methods.BPP import BPP
from search_methods.BPPV import BPPV, BPPVConfig
from search_methods.GlobalHeuristic import GlobalHeuristic
from search_methods.LocalHeuristic import LocalHeuristic


class Config:
    dic_algorithms = {}
    dic_heuristics = None

    def __init__(self, algorithm: str, discs: int = 7, BPPV_config: BPPVConfig = None, heuristics: str = None):
        self.algorithm = algorithm
        self.heuristics = heuristics
        self.discs = discs
        self.BPPV_config = BPPV_config

        if heuristics is not None:
            self.dic_heuristics = {}
            self.load_heuristics()

        self.load_algorithms()

    def get_algorithm(self):
        h = self.heuristics if self.heuristics is None else self.dic_heuristics[self.heuristics]
        return self.dic_algorithms[self.algorithm](h)

    def load_algorithms(self):
        self.dic_algorithms['BPA'] = lambda x: BPA(self)
        self.dic_algorithms['BPP'] = lambda x: BPP(self)
        self.dic_algorithms['BPPV'] = lambda x: BPPV(self)
        self.dic_algorithms['AStar'] = lambda x: AStar(self,x)
        self.dic_algorithms['GlobalHeuristic'] = lambda x: GlobalHeuristic(self,x)
        self.dic_algorithms['LocalHeuristic'] = lambda x: LocalHeuristic(self,x)

    def load_heuristics(self):
        self.dic_heuristics['Basic'] = DiscsOnTheLastTower()

    def __str__(self) -> str:
        return f'algorithm: {self.algorithm}\nheuristics: {self.heuristics}'
