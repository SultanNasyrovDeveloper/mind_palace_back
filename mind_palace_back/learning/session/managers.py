from datetime import datetime, timedelta

from django.conf import settings
from django.db import models

from mind_palace_back.learning.session.enums import UserLearningSessionStatusEnum
from mind_palace_back.learning.stats.models import NodeLearningStatistics


class UserLearningSessionManager(models.Manager):

    def start(self, **session_data) -> 'UserLearningSession':
        """
        Start new learning session.

        Args:
            session_data: Field values for new session that will be created.
            Must be validated before. Use UserLearningSessionSerializer.
        """
        session = self.create(**session_data)
        session.queue = session.get_strategy().generate_learning_queue(session.root)
        session.save()
        return session

    def study_node(self, session, **kwargs):
        """
        Handle study node by user.
        """
        # TODO: Maybe make atomic.
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
        if not session.repeated_nodes:
            session.delete()
            return
        session.queue = []
        session.finish_datetime = datetime.utcnow()
        session.status = UserLearningSessionStatusEnum.finished
        session.save()
        return session

    def finish_bulk(self, sessions):
        """
        Finish all sessions in given queryset.

        Args:
            sessions: Session queryset.
        """
        sessions.update(
            status=UserLearningSessionStatusEnum.finished,
            queue=[],
            finish_datetime=datetime.utcnow()
        )

    def finish_expired(self, initial_queryset=None, **query_params) -> None:
        """
        Close/finish all expired session filtered by given query params.

        First filter all session by given query parameters then close all expired session among them.

        Args:
            initial_queryset: Initial sessions queryset.
            query_params: Django like query params will be put in manager filter method.
        """
        initial_queryset = initial_queryset or self.all()
        target_sessions = initial_queryset.filter(**query_params)
        expired_sessions = target_sessions.filter(
            last_repetition_datetime__lt=datetime.utcnow() - timedelta(
                minutes=settings.USER_LEARNING_SESSION_EXPIRE
            )
        )
        self.finish_bulk(expired_sessions)


