from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for registering new users.

    Fields:
        - username: required string
        - email: optional string
        - password: required string, write-only (won't appear in responses)

    This serializer uses Django's built-in User model and safely
    hashes the password using the `create_user` method.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        """
        Create a new user instance with a hashed password.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
