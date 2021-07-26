from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mind_palace_back.learning.session import models, serializers
from mind_palace_back.learning.session.enums import UserLearningSessionStatusEnum


class LearningSessionViewSet(ModelViewSet):

    queryset = models.UserLearningSession.objects.all()
    serializer_class = serializers.UserLearningSessionSerializer

    @action(detail=False, methods=('GET', ))
    def my_active_session(self, request, *args, **kwargs):
        response_data = None
        models.UserLearningSession.objects.finish_expired(user_id=request.user.id)
        target_session = self.queryset.filter(
            user=request.user.id, status=UserLearningSessionStatusEnum.active
        ).first()
        if target_session:
            response_data = self.serializer_class(target_session).data
        return Response(response_data)

    @action(detail=False, methods=('POST', ))
    def start(self, request, *args, **kwargs):
        """
        Start new learning session.
        """
        # TODO: Make atomic
        models.UserLearningSession.objects.finish_expired(user_id=request.user.id)
        user_active_sessions = models.UserLearningSession.objects.filter(
            status=UserLearningSessionStatusEnum.active
        )
        if user_active_sessions:
            models.UserLearningSession.objects.finish_bulk(user_active_sessions)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        # TODO: Probably there is an easier way to add user to data.
        session_data = dict(serializer.validated_data)
        session_data['user_id'] = request.user.id
        new_session = models.UserLearningSession.objects.start(**session_data)
        return Response(self.serializer_class(new_session).data)

    @action(detail=True, methods=('GET', ))
    def current(self, request, *args, **kwargs):
        """
        Retrieve current learning node.
        """
        return Response(self.get_object().get_current_node_id())

    @action(detail=True, methods=('GET', ))
    def next(self, request, *args, **kwargs):
        """
        Retrieve next node to learn.
        """
        return Response(self.get_object().get_next_node_id())

    @action(detail=True, methods=('POST', ))
    def study_node(self, request, *args, **kwargs):
        """
        Handle node studying.
        """
        session = self.get_object()
        serializer = serializers.NodeStudyDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        models.UserLearningSession.objects.study_node(session, **serializer.validated_data)
        return Response({'status': 200, 'next': session.get_current_node_id()})

    @action(detail=True, methods=('POST',))
    def finish(self, request, *args, **kwargs):
        session = models.UserLearningSession.objects.finish(self.get_object())
        return Response(
            serializers.UserLearningSessionSerializer(session).data
        )

