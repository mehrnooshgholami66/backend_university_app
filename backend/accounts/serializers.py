from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth import authenticate


User = get_user_model()

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

