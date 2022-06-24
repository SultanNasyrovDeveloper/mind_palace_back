from rest_framework.viewsets import ModelViewSet

from .. import models, serializers


class NodeBodyViewSet(ModelViewSet):
    queryset = models.Body.objects.all()
    serializer_class = serializers.NodeBodySerializer
