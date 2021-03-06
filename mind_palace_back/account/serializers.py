from rest_framework import serializers

from mind_palace_back.account import models


class UserSignUpCredentialsSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        return models.User.objects.create_user(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    mind_palace_root = serializers.IntegerField(source='mypalace.root_id')

    class Meta:
        model = models.User
        fields = '__all__'
