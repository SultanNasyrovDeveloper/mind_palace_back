from rest_framework import viewsets

from mind_palace_back.palace.node import models, serializers


class MindPalaceNodeViewSet(viewsets.ModelViewSet):

    queryset = models.MindPalaceNode.objects.all()
    serializer_class = serializers.MindPalaceNodeSerializer
