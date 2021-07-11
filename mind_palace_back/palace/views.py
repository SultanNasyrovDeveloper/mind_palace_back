from rest_framework.viewsets import ModelViewSet

from mind_palace_back.palace import models, serializers


class UserMindPalaceViewSet(ModelViewSet):

    queryset = models.UserMindPalace.objects.all()
    serializer_class = serializers.UserMindPalaceSerializer
