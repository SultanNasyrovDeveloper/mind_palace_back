from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from mind_palace.palace.node import models
from mind_palace.learning.stats.serializers import UserLearningStatisticsSerializer


class NodeMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MindPalaceNodeMedia
        exclude = ('image', )


class NodeBodySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NodeBody
        fields = ('id', 'type', 'meta', 'data')

    def update(self, instance, validated_data):
        if 'type' in validated_data:
            validated_data['meta'] = {}
            validated_data['data'] = {}
        if 'meta' in validated_data:
            validated_data['meta'] = {**instance.meta, **validated_data.get('meta', {})}
        if 'data' in validated_data:
            validated_data['data'] = {**instance.data, **validated_data.get('data', {})}
        return super().update(instance, validated_data)


class NodeBriefInfoSerializer(serializers.ModelSerializer):
    """
    Serializes only nodes basic information.
    """

    class Meta:
        model = models.MindPalaceNode
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
        model = models.MindPalaceNode
        fields = (
            'id', 'ancestors', 'learning_statistics', 'media', 'name', 'title',
            'children', 'parent', 'owner', 'body'
        )
        read_only_fields = ('children', )

    def get_ancestors(self, node):
        """
        Get list of ancestors.
        """
        return [
            {'id': ancestor.id, 'text': ancestor.name}
            for ancestor in node.get_ancestors(include_self=True)
        ]


class TreeNodeSerializer(serializers.Serializer):

    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField()
    name = serializers.CharField()
    children = serializers.ListField(child=RecursiveField(), source='get_children')
    learning_statistics = UserLearningStatisticsSerializer(read_only=True)
