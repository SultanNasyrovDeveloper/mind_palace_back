from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from mind_palace.palace.node import models
from mind_palace.learning.stats.serializers import UserLearningStatisticsSerializer


class NodeMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.MindPalaceNodeMedia
        exclude = ('image', )


class NoteTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NodeTag
        fields = '__all__'


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
    # TODO: Refactor NoteTagSerializer init params
    tags = NoteTagSerializer(many=True, allow_null=True, default=list, read_only=True)
    learning_statistics = UserLearningStatisticsSerializer(read_only=True)
    # TODO: make media on expand or at other endpoint,
    media = NodeMediaSerializer(many=True, read_only=True)
    # children = serializers.ListField(child=RecursiveField(), source='get_children', read_only=True)

    class Meta:
        model = models.MindPalaceNode
        fields = '__all__'

    def get_ancestors(self, neuron):
        """
        Get list of ancestors.
        """
        return [
            {'id': ancestor.id, 'text': ancestor.name}
            for ancestor in neuron.get_ancestors(include_self=True)
        ]

    def update(self, instance, validated_data):
        if 'body_type' in validated_data:
            instance.body = {}
        if 'body' in validated_data:
            instance.body.update(validated_data.pop('body'))
        return super().update(instance, validated_data)


class MindPalaceTreeNodeSerializer(serializers.Serializer):

    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField()
    name = serializers.CharField()
    children = serializers.ListField(child=RecursiveField(), source='get_children')
    learning_statistics = UserLearningStatisticsSerializer(read_only=True)
