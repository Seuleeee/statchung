from django.forms import CharField
from pkg_resources import require
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_jwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

User = get_user_model()


class UserCreateSerializer(serializers.Serializer):
    user_id = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def create(self, validated_data):
        user = User.objects.create(
            user_id=validated_data['user_id'],
            email=validated_data['email'],
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])

        user.save()
        return user


JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        user_id = data.get("user_id", None)
        password = data.get("password", None)
        user = authenticate(user_id=user_id, password=password)

        if user is None:
            return {
                'user_id': 'None'
            }
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)  # 토큰 발행

            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given user_id and password does not exists'
            )
        return {
            'user_id': user.user_id,
            'token': jwt_token
        }


class LoginRequestSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    password = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    user_id = serializers.CharField()
    token = serializers.CharField()
