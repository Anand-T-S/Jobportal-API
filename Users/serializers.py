from rest_framework.serializers import ModelSerializer
from Users.models import User
from rest_framework import serializers


class RegistrationSerializer(ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "phone",
            "role"
        ]

    def create(self, validated_data):                             # password hashed
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

