from mind_palace_back.learning.strategy.enums import MindPalaceLearningStrategiesEnum
from mind_palace_back.learning.strategy.supermemo2 import SuperMemo2LearningStrategy

# TODO: Autodiscover
strategies_map = {
    MindPalaceLearningStrategiesEnum.supermemo_2: SuperMemo2LearningStrategy
}


class UserLearningStrategyFactory:

    @classmethod
    def create(cls, strategy_name, **strategy_configuration):
        assert MindPalaceLearningStrategiesEnum.contains(strategy_name)
        return strategies_map.get(strategy_name)()
