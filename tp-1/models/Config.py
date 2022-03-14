from heuristics.AdmissibleEstimatedPossibleMovements import AdmissibleEstimatedPossibleMovements
from heuristics.DiscsOnTheLastTower import DiscsOnTheLastTower
from heuristics.EstimatedPossibleMovements import EstimatedPossibleMovements
from search_methods.AStar import AStar
from search_methods.BPA import BPA
from search_methods.BPP import BPP
from search_methods.BPPV import BPPV, BPPVConfig
from search_methods.GlobalHeuristic import GlobalHeuristic
from search_methods.LocalHeuristic import LocalHeuristic


class Config:
    dic_algorithms = {}
    dic_heuristics = None

    def __init__(self, algorithm: str, discs: int = 7, BPPV_config: BPPVConfig = None, heuristics: str = None, print_to: str = "console"):
        self.algorithm = algorithm
        self.heuristics = heuristics
        self.discs = discs
        self.BPPV_config = BPPV_config
        self.print_to = print_to

        if heuristics is not None:
            self.dic_heuristics = {}
            self.load_heuristics()

        self.load_algorithms()

    def get_algorithm(self):
        h = self.dic_heuristics[self.heuristics]() if self.heuristics is not None else None
        return self.dic_algorithms[self.algorithm](h)

    def load_algorithms(self):
        self.dic_algorithms['BPA'] = lambda x: BPA(self)
        self.dic_algorithms['BPP'] = lambda x: BPP(self)
        self.dic_algorithms['BPPV'] = lambda x: BPPV(self)
        self.dic_algorithms['AStar'] = lambda x: AStar(self, x)
        self.dic_algorithms['GlobalHeuristic'] = lambda x: GlobalHeuristic(self, x)
        self.dic_algorithms['LocalHeuristic'] = lambda x: LocalHeuristic(self, x)

    def load_heuristics(self):
        self.dic_heuristics['DiscsOnTheLastTower'] = lambda: DiscsOnTheLastTower()
        self.dic_heuristics['AdmissibleEstimatedPossibleMovements'] = lambda: AdmissibleEstimatedPossibleMovements()
        self.dic_heuristics['EstimatedPossibleMovements'] = lambda: EstimatedPossibleMovements()

    def print_to_console(self) -> bool:
        return self.print_to == "console"

    def print_to_file(self) -> bool:
        return self.print_to != "console"

    def __str__(self) -> str:
        value = f"Algorithm: {self.algorithm}\n" \
                f"Number of discs: {self.discs}\n"

        value += {
            "BPA": lambda:"",
            "BPP": lambda:"",
            "BPPV": lambda: f"Max Depth: {self.BPPV_config['max_depth']}\nDepth Modifier: {self.BPPV_config['depth_modifier']}",
            "AStar": lambda:f"Heuristic: {self.heuristics}",
            "GlobalHeuristic": lambda:f"Heuristic: {self.heuristics}",
            "LocalHeuristic":lambda: f"Heuristic: {self.heuristics}"
        }[self.algorithm]()

        return value
