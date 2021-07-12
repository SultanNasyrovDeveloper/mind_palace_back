from rest_framework import serializers

from mind_palace_back.palace import models


class UserMindPalaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserMindPalace
        fields = '__all__'


class MindPalaceTreeSerializer(serializers.Serializer):

    def to_representation(self, instance):
        pass

    def to_internal_value(self, data):
        pass