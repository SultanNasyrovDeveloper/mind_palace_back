from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from mind_palace.palace.node import models, serializers
from mind_palace.learning.stats.models import NodeLearningStatistics


class MindPalaceNodeViewSet(viewsets.ModelViewSet):

    queryset = models.MindPalaceNode.objects.all()
    serializer_class = serializers.MindPalaceNodeSerializer

    def has_permission(self, request, view, obj):
        return True

    def retrieve(self, request, pk=None):
        if not pk:
            return super().retrieve(request)
        node = get_object_or_404(models.MindPalaceNode, pk=pk)
        stats = NodeLearningStatistics.objects.get(node_id=node.id)
        stats.views += 1
        stats.save()
        return Response(self.serializer_class(node).data)

    @action(
        detail=True,
        methods=('POST', ),
        serializer_class=serializers.MindPalaceNodeAddMediaDataSerializer,
    )
    def add_media(self, request, *args, **kwargs):
        return Response({})

