from datetime import datetime

from django.db import models

from mind_palace_back.learning.session.enums import UserLearningSessionStatusEnum
from mind_palace_back.learning.stats.models import NodeLearningStatistics


class UserLearningSessionManager(models.Manager):

    def start(self, session_data):
        """
        Start new learning session.
        """
        session = self.create(**session_data)
        strategy = session.get_strategy()
        session.queue = strategy.generate_learning_queue(session.root)
        session.save()
        return session

    def study_node(self, session, **kwargs):
        """
        Handle study node by user.
        """
        # TODO: Maybe make atomic.
        # TODO: Probably this method should accept node as an argument not an id
        node_id = kwargs.pop('node')
        node_learning_stats = NodeLearningStatistics.objects.get(node_id=node_id)
        session.get_strategy().study_node(node_learning_stats, **kwargs)
        session.last_repetition_datetime = datetime.utcnow()
        session.remove_node_from_queue(node_id)
        session.add_repeated_node(node_id)
        session.save()
        return session

    def finish(self, session):
        """
        Finish given session.
        """
        session.queue = []
        session.finish_datetime = datetime.utcnow()
        session.status = UserLearningSessionStatusEnum.finished
        session.save()
        return session
