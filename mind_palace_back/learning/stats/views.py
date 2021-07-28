from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mind_palace_back.learning.stats import models, serializers


class NodeLearningStatisticsViewSet(ModelViewSet):

    queryset = models.NodeLearningStatistics.objects.all()
    serializer_class = serializers.UserLearningStatisticsSerializer

    @action(detail=False, methods=('GET', ))
    def node_statistics(self, request, *args, **kwargs):
        node_id = request.GET.get('node_id', None)
        if not node_id:
            raise ValidationError(
                'You must specify node id as query param in order to retrieve statistics.'
            )
        try:
            node_stats = self.queryset.get(node_id=node_id)
        except models.NodeLearningStatistics.DoesNotExist:
            raise ValidationError('Stats related to this node does not exist.')
        return Response(self.serializer_class(node_stats).data)