from rest_framework.serializers import ModelSerializer

from mind_palace_back.palace import models


class UserMindPalaceSerializer(ModelSerializer):

    class Meta:
        model = models.UserMindPalace
        fields = '__all__'
