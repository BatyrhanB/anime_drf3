from rest_framework import response, status, generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response

from .models import User
from .serializers import (
    UserSerializer,
    RegistrationSerializer
    )
from .utils import Util


class RegistrationAPIView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        current_site = get_current_site(
        request=request).domain
        user_data = serializers.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        abs_url = f'http:// + {current_site}/api/v1/users/verify-email/'+ '?token=' + str(token)
        email_body = f'Hello' \
                     f'Use this link to activate your email\n ' \
                     f'The link will be active for 10 minutes \n {abs_url}'
        data = {'email_body': email_body, 'to_email': user.email,
            'email_subject': 'Verify your email'}
        Util.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)


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

