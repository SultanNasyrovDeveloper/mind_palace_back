from rest_framework import serializers

from mind_palace.palace import models
from mind_palace.palace.node.models import PalaceNode

from .enums import MoveToPositionChoices


class UserMindPalaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserMindPalace
        fields = '__all__'


class PalaceNodeMoveDataSerializer(serializers.Serializer):

    node = serializers.PrimaryKeyRelatedField(
        queryset=PalaceNode.objects.all()
    )
    target = serializers.PrimaryKeyRelatedField(
        queryset=PalaceNode.objects.all()
    )
    position = serializers.ChoiceField(
        choices=MoveToPositionChoices.choices()
    )