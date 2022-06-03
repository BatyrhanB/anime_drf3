from drf_yasg.utils import swagger_auto_schema
from rest_framework import serializers, status

from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name','is_staff','is_active','is_email_confirmed','date_joined')
        read_only_fields = ('date_joined',)


class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('style', {})

        kwargs['style']['input_type'] = 'password'
        kwargs['write_only'] = True

        super().__init__(*args, **kwargs)


class RegistrationSerializer(serializers.ModelSerializer):

    password = PasswordField(required=True, allow_blank=False, allow_null=False)
    password2 = PasswordField(required=True, allow_blank=False, allow_null=False)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'password', 'password2', 'first_name', 'last_name']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        account = User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Password must much'}
            )
        account.set_password(password)
        account.save()
        return account


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class LoginResponseSerializer(serializers.Serializer):
    user = UserSerializer()
    refresh = serializers.CharField()
    access = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False, allow_null=False)
    password = PasswordField(required=True, allow_blank=False, allow_null=False)


