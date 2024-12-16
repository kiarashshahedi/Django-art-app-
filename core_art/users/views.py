from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
import random
from .serializers import UserRegistrationSerializer, OTPSerializer, VerifyOTPSerializer
from .models import User
from datetime import time

# OTP REGISTERING
class GenerateOTPView(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data['mobile']
        user = User.objects.get(mobile=mobile)
        user.otp = f'{random.randint(100000, 999999)}'
        user.otp_created_at = now()
        user.save()
        # Simulate sending OTP (print to console or use SMS service)
        print(f"Your OTP is {user.otp}")
        return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)

class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(mobile=serializer.validated_data['mobile'])
        user.otp = None
        user.otp_created_at = None
        user.save()

        # Generate JWT
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }, status=status.HTTP_200_OK)
    
# Register User View
class UserRegistrationView(APIView):

    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            tokens = RefreshToken.for_user(user)

            return Response({
                'message': 'User registered successfully.',
                'refresh': str(tokens),
                'access': str(tokens.access_token),
            }, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
