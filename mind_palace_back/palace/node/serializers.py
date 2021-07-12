from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from mind_palace_back.palace.node import models


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

    tags = NoteTagSerializer(many=True, allow_null=True, default=list, read_only=True)

    class Meta:
        model = models.MindPalaceNode
        fields = '__all__'


class MindPalaceTreeNodeSerializer(serializers.Serializer):

    parent = serializers.PrimaryKeyRelatedField(read_only=True)
    id = serializers.IntegerField()
    name = serializers.CharField()
    children = serializers.ListField(child=RecursiveField(), source='get_children')
