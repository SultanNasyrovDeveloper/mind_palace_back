from datetime import datetime

from django.db import models
from django.contrib.postgres.fields import ArrayField

from mind_palace_back.learning.session.enums import UserLearningSessionStatusEnum
from mind_palace_back.learning.session.managers import UserLearningSessionManager
from mind_palace_back.learning.strategy.enums import MindPalaceLearningStrategiesEnum
from mind_palace_back.learning.strategy.factory import UserLearningStrategyFactory


class UserLearningSession(models.Model):
    """
    User learning session.
    """

    status = models.CharField(
        max_length=100, choices=UserLearningSessionStatusEnum.choices(),
        default=UserLearningSessionStatusEnum.active,
    )
    user = models.ForeignKey(
        'account.User', on_delete=models.CASCADE, related_name='learning_sessions',
    )
    strategy_name = models.CharField(
        max_length=1000, choices=MindPalaceLearningStrategiesEnum.choices(),
        default=MindPalaceLearningStrategiesEnum.supermemo_2,
    )

    root = models.ForeignKey('node.MindPalaceNode', on_delete=models.CASCADE)
    queue = ArrayField(models.IntegerField(), default=list)
    repeated_nodes = ArrayField(models.IntegerField(), default=list)

    start_datetime = models.DateTimeField(default=datetime.utcnow)
    finish_datetime = models.DateTimeField(null=True, default=None)
    last_repetition_datetime = models.DateTimeField(default=datetime.utcnow)

    objects = UserLearningSessionManager()

    def get_strategy(self):
        return UserLearningStrategyFactory.create(self.strategy_name)

    def get_current_node_id(self):
        try:
            return self.queue[0]
        except IndexError:
            return None

    def get_next_node_id(self):
        try:
            return self.queue[1]
        except IndexError:
            return None

    def remove_node_from_queue(self, node_id):
        if node_id in self.queue:
            self.queue.remove(node_id)

    def add_repeated_node(self, node_id):
        self.repeated_nodes.append(node_id)
