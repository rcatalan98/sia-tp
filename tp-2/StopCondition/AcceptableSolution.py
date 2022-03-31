from StopCondition.BaseStopCondition import BaseStopCondition


class AcceptableSolution(BaseStopCondition):
    def has_to_stop(self):
        config: AcceptableSolutionConfig = self.config
        return max([p.fitness for p in self.pool_manager.population]) >= config.acceptable_benefit


class AcceptableSolutionConfig:
    def __init__(self, acceptable_benefit: int):
        self.acceptable_benefit = acceptable_benefit
