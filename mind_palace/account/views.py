from rest_framework import views, viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from mind_palace.account import serializers, models


class SignUpView(views.APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user_serializer = serializers.UserSignUpCredentialsSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        try:
            user_serializer.save()
        except Exception as e:
            raise ValidationError(str(e))
        return Response({'Created': True}, status=201)


class UserViewSet(viewsets.ModelViewSet):

    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(detail=False, methods=('GET', ))
    def me(self, request, *args, **kwargs):
        return Response(self.serializer_class(request.user).data)
