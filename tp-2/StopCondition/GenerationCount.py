from StopCondition.BaseStopCondition import BaseStopCondition


class GenerationCount(BaseStopCondition):

    def has_to_stop(self):
        config: GenerationCountConfig = self.config
        max_generations: int = config.max_generation
        return max_generations <= self.pool_manager.generation


class GenerationCountConfig:
    def __init__(self, max_generation):
        self.max_generation = max_generation
