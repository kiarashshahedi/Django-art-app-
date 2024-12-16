from rest_framework import serializers
from .models import User
from django.core.exceptions import ValidationError
from django.utils.timezone import now, timedelta

# OTP
class OTPSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)

    def validate_mobile(self, mobile):
        if not User.objects.filter(mobile=mobile).exists():
            User.objects.create_user(mobile=mobile)
        return mobile

# Verify otp
class VerifyOTPSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        user = User.objects.filter(mobile=data['mobile'], otp=data['otp']).first()
        if not user or user.otp_created_at < now() - timedelta(minutes=10):
            raise serializers.ValidationError("Invalid or expired OTP")
        return data
    
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