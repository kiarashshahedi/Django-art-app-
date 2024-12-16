from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError


# User Registering serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile', 'password', 'is_seller', 'is_buyer']

    # Create User
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            mobile=validated_data['mobile'],
            is_seller=validated_data.get('is_seller', False),
            is_buyer=validated_data.get('is_buyer', False),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user