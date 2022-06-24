from rest_framework import serializers

from mind_palace.palace.node.models import PalaceNode
from mind_palace.learning.session import models
from mind_palace.learning.strategy.enums import MindPalaceLearningStrategiesEnum


class UserLearningSessionSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    root = serializers.PrimaryKeyRelatedField(queryset=PalaceNode.objects.all())
    strategy_name = serializers.ChoiceField(choices=MindPalaceLearningStrategiesEnum.choices())
    current = serializers.IntegerField(source='get_current_node_id', read_only=True)

    class Meta:
        model = models.UserLearningSession
        fields = (
            'id', 'status', 'start_datetime', 'finish_datetime', 'last_repetition_datetime', 'root',
            'strategy_name', 'user', 'current', 'total_repetitions', 'average_rating'
        )
        read_only_fields = (
            'id', 'status', 'start_datetime', 'finish_datetime', 'last_repetition_datetime', 'user',
            'current'
        )


class NodeStudyDataSerializer(serializers.Serializer):

    node = serializers.IntegerField()
    rating = serializers.IntegerField(min_value=1, max_value=6)
