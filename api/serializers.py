from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import TextPost
from django.contrib.auth import authenticate

#Custom Username Token
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Authenticate by email, not username
        user = authenticate(request=self.context.get('request'), username=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")

        # Generate the token
        data = super().validate(attrs)
        data['email'] = user.email  # You want to include email
        data['fullname'] = f"{user.first_name} {user.last_name}"  # Add full name
        return data

# User Registration Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is not exposed
        }

    def create(self, validated_data):
        # Extract fields for clarity
        first_name = validated_data.pop('first_name', None)
        last_name = validated_data.pop('last_name', None)
        email = validated_data.get('email')
        # username = validated_data.get('username')
        password = validated_data.get('password')

        # Create the user with the provided fields
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,
            password=password
        )
        return user

# JWT Token Serializer
class TokenSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()

# TextPost Serializer
class TextPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPost
        fields = ['id', 'text', 'user', 'created_at']
        read_only_fields = ['user']
