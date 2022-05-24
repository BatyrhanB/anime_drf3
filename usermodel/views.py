from rest_framework import response, status, generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    UserSerializer,
    )

class ProfileAPIView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={'200': UserSerializer()}, tags=['auth'])
    def get(self, request):
        user = request.user
        serializer = self.get_serializer(instance=request.user)
        return response.Response(data=serializer.data)

    def patch(self, request):
        serializer = self.get_serializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(data=get_login_response(request.user, request.data))
    
    def delete(self, request):
        request.user.delete()
        return response.Response(status.HTTP_200_OK)

