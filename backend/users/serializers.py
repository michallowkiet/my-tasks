from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("id", "email", "username")


class SignUpUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=True, validators=[validate_password]
    )

    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, required=True, validators=[validate_password]
    )

    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=CustomUser.objects.all())])

    class Meta:
        model = CustomUser
        fields = ("email", "username", "password", "password2")

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.pop("password2")
        if password != password2:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data["password"])
        user.save()

        return user


class SignInUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(style={"input_type": "password"}, write_only=True, required=True)

    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
