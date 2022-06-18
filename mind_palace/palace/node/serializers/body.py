from rest_framework import serializers

from mind_palace.palace.node import models


class NodeBodySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.NodeBody
        fields = ('id', 'type', 'meta', 'data')

    def update(self, instance, validated_data):
        if 'type' in validated_data:
            validated_data['meta'] = {}
            validated_data['data'] = {}
        if 'meta' in validated_data:
            validated_data['meta'] = {**instance.meta, **validated_data.get('meta', {})}
        if 'data' in validated_data:
            validated_data['data'] = {**instance.data, **validated_data.get('data', {})}
        return super().update(instance, validated_data)


