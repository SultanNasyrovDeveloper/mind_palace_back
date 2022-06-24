from rest_framework.viewsets import ModelViewSet

from mind_palace.palace.node.models import Media
from mind_palace.palace.node.serializers import NodeMediaSerializer


class MindPalaceNodeMediaViewSet(ModelViewSet):

    queryset = Media.objects.all()
    serializer_class = NodeMediaSerializer
