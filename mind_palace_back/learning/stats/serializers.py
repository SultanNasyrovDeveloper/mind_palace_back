from rest_framework import serializers

from mind_palace_back.learning.stats import models


class UserLearningStatisticsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NodeLearningStatistics
        fields = '__all__'
