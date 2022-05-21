from datetime import datetime

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from mind_palace.palace.node import models, serializers, filters


class MindPalaceNodeViewSet(viewsets.ModelViewSet):

    queryset = models.MindPalaceNode.objects.all()
    serializer_class = serializers.MindPalaceNodeSerializer
    filterset_class = filters.MindPalaceNodeFilter

    def retrieve(self, request, pk=None, *args, **kwargs):
        """
        Updates node views everytime use sees its own node.
        """
        node = self.get_object()
        if node.owner_id == request.user.id:
            node.learning_statistics.views += 1
            node.learning_statistics.last_view = datetime.utcnow()
            node.learning_statistics.save()
        return Response(self.serializer_class(node).data)

    def create(self, request, *args, **kwargs):
        data = dict(request.data)
        data['owner'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(
        detail=True,
        methods=('POST', ),
        serializer_class=serializers.NodeMediaSerializer,
    )
    def add_media(self, request, *args, **kwargs):
        request_data = dict(request.data)
        request_data['node'] = self.get_object().id
        serializer = self.get_serializer_class()(data=request_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
