from rest_framework import views
from rest_framework.response import Response

from mind_palace_back.account import serializers


class SignUpView(views.APIView):

    def post(self, request, *args, **kwargs):
        user_serializer = serializers.UserSignUpCredentialsSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        return Response({'status': 201})




