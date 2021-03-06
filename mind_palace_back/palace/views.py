from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from mind_palace_back.palace import models, serializers
from mind_palace_back.palace.node.filters import MindPalaceNodeFilter
from mind_palace_back.palace.node.models import MindPalaceNode
from mind_palace_back.palace.node.serializers import MindPalaceTreeNodeSerializer


class UserMindPalaceViewSet(ModelViewSet):

    queryset = models.UserMindPalace.objects.all()
    serializer_class = serializers.UserMindPalaceSerializer
    filterset_class = MindPalaceNodeFilter

    @action(detail=False, methods=('GET', ))
    def my_palace(self, request, *args, **kwargs):
        return self.serializer_class(request.user.mypalace).data

    @action(detail=False, methods=('GET', ))
    def tree(self, request, *args, **kwargs):
        root_id = request.GET.get('root', None)
        if not root_id:
            raise ValidationError('Root must be specified.')
        depth = request.GET.get('depth', 3)
        root_node = MindPalaceNode.objects.get(id=root_id)
        cached_tree_root = root_node.get_descendants(include_self=True).filter(
            level__lt=root_node.level + int(depth)
        ).get_cached_trees()[0]
        serializer = MindPalaceTreeNodeSerializer(cached_tree_root)
        return Response(serializer.data)
