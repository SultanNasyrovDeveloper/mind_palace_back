from rest_framework import serializers

from mind_palace.palace import models
from mind_palace.palace.node.models import MindPalaceNode

from .enums import MoveToPositionChoices


class UserMindPalaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserMindPalace
        fields = '__all__'


class PalaceNodeMoveDataSerializer(serializers.Serializer):

    node = serializers.PrimaryKeyRelatedField(
        queryset=MindPalaceNode.objects.all()
    )
    target = serializers.PrimaryKeyRelatedField(
        queryset=MindPalaceNode.objects.all()
    )
    position = serializers.ChoiceField(
        choices=MoveToPositionChoices.choices()
    )