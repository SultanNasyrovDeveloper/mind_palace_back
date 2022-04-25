from rest_framework.viewsets import ModelViewSet

from mind_palace.palace.node.models import MindPalaceNodeMedia
from mind_palace.palace.node.serializers import NodeMediaSerializer


class MindPalaceNodeMediaViewSet(ModelViewSet):

    queryset = MindPalaceNodeMedia.objects.all()
    serializer_class = NodeMediaSerializer
