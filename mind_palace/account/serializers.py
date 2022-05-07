from rest_framework import serializers

from . import models


class UserSignUpCredentialsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = ('username', 'password')

    def create(self, validated_data):
        return models.User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    mind_palace_root = serializers.IntegerField(source='mypalace.root_id')

    class Meta:
        model = models.User
        exclude = ('password', )
