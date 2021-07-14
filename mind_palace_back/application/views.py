from rest_framework.views import APIView
from rest_framework.response import Response

from mind_palace_back.palace.node.enums import NodeBodyTypeEnum


class EnumsApiView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({'node_body_types': NodeBodyTypeEnum.choices()})
