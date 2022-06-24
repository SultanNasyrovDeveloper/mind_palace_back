from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from mind_palace.palace.node import models
from mind_palace.learning.stats.serializers import UserLearningStatisticsSerializer

from .media import NodeMediaSerializer
from .body import NodeBodySerializer


class NodeBriefInfoSerializer(serializers.ModelSerializer):
    """
    Serializes only nodes basic information.
    """

    class Meta:
        model = models.PalaceNode
        fields = ('id', 'name', 'parent')


class MindPalaceNodeSerializer(serializers.ModelSerializer):
    """
    Provide full mind palace node information.
    """
    ancestors = serializers.SerializerMethodField(read_only=True)
    learning_statistics = UserLearningStatisticsSerializer(read_only=True)
    media = NodeMediaSerializer(many=True, read_only=True)
    body = NodeBodySerializer(read_only=True)

    class Meta:
        model = models.PalaceNode
        fields = (
            'id', 'ancestors', 'learning_statistics', 'media', 'name', 'description',
            'children', 'parent', 'owner', 'body'
        )
        read_only_fields = ('children', )

    def get_ancestors(self, node):
        """
        Get list of ancestors.
        """
        return [
            {'id': ancestor.id, 'name': ancestor.name}
            for ancestor in node.get_ancestors(include_self=True)
        ]


class TreeNodeSerializer(serializers.Serializer):

    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField()
    name = serializers.CharField()
    children = serializers.ListField(child=RecursiveField(), source='get_children')
    learning_statistics = UserLearningStatisticsSerializer(read_only=True)
