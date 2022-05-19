from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from mind_palace.palace import models, serializers
from mind_palace.palace.node.models import MindPalaceNode
from mind_palace.palace.node.serializers import TreeNodeSerializer


class UserMindPalaceViewSet(ModelViewSet):

    queryset = models.UserMindPalace.objects.all()
    serializer_class = serializers.UserMindPalaceSerializer
