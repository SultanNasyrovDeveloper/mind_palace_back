from rest_framework import serializers

from mind_palace.palace.node.models import MindPalaceNode
from mind_palace.learning.session import models
from mind_palace.learning.strategy.enums import MindPalaceLearningStrategiesEnum


class UserLearningSessionSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    root = serializers.PrimaryKeyRelatedField(queryset=MindPalaceNode.objects.all())
    strategy_name = serializers.ChoiceField(choices=MindPalaceLearningStrategiesEnum.choices())

    class Meta:
        model = models.UserLearningSession
        fields = (
            'id', 'status', 'start_datetime', 'finish_datetime', 'last_repetition_datetime', 'root',
            'strategy_name', 'user', 'queue'
        )
        read_only_fields = (
            'id', 'status', 'start_datetime', 'finish_datetime', 'last_repetition_datetime', 'user',
            'queue'
        )


class NodeStudyDataSerializer(serializers.Serializer):

    node = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=6)