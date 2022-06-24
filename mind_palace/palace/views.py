from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from mind_palace.palace import models, serializers
from mind_palace.palace.node.models import PalaceNode
from mind_palace.palace.node.serializers import TreeNodeSerializer


class UserMindPalaceViewSet(ModelViewSet):

    queryset = models.UserMindPalace.objects.all()
    serializer_class = serializers.UserMindPalaceSerializer

    @action(detail=False, methods=('GET',))
    def tree(self, request, *args, **kwargs):
        root_id = request.GET.get('root', None)
        if not root_id:
            raise ValidationError('Root must be specified.')
        depth = request.GET.get('depth', 3)
        root_node = PalaceNode.objects.get(id=root_id)
        subtree_query = (
            root_node
                .get_descendants(include_self=True)
                .filter(level__lt=root_node.level + int(depth))
                .select_related('learning_statistics')
        )
        cached_subtree = subtree_query.get_cached_trees()[0]
        serializer = TreeNodeSerializer(cached_subtree)
        return Response(serializer.data)

    @action(
        detail=False,
        methods=('POST', ),
        serializer_class=serializers.PalaceNodeMoveDataSerializer
    )
    def move_node(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        PalaceNode.objects.move_node(**serializer.validated_data)
        return Response()
