
from Breeding.MultipleBreeder import MultipleBreeder, MultipleBreederConfig
from Breeding.SimpleBreeder import SimpleBreeder
from Breeding.UniformBreeder import UniformBreeder
from Selection.EliteSelection import EliteSelection
from Selection.RankSelection import RankSelection
from Selection.RouletteSelection import RouletteSelection
from Selection.TournamentSelection import TournamentSelection
from Selection.TruncatedSelection import TruncatedSelection


class AlgorithmConfig:
    breeding_algorithms = {}
    selection_algorithms = {}

    def __init__(self, breeding: str, selection: str, population_size: int, ) -> None:
        self.breeding = breeding
        self.selection = selection
        self.population_size = population_size

    def load_breeding_algorithms(self):
        # loading breeding algorithms
        self.breeding_algorithms['SimpleBreeder'] = lambda x: SimpleBreeder()
        self.breeding_algorithms['MultipleBreeder'] = lambda x: MultipleBreeder(self, x)
        self.breeding_algorithms['UniformBreeder'] = lambda x: UniformBreeder()

    def load_selection_algorithms(self):
        self.selection_algorithms['EliteSelection'] = lambda x: EliteSelection()
        self.selection_algorithms['RankSelection'] = lambda x: RankSelection()
        self.selection_algorithms['RouletteSelection'] = lambda x: RouletteSelection()
        self.selection_algorithms['TournamentSelection'] = lambda x: TournamentSelection()
        self.selection_algorithms['TruncatedSelection'] = lambda x: TruncatedSelection()
