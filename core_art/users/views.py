from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
import random
from .serializers import UserRegistrationSerializer, OTPSerializer, VerifyOTPSerializer
from .models import User
from django.utils.timezone import now, timedelta

# OTP REGISTERING
class GenerateOTPView(APIView):
    def post(self, request):
        serializer = OTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data['mobile']

        user, created = User.objects.get_or_create(mobile=mobile)
        user.otp = f'{random.randint(100000, 999999)}'
        user.otp_created_at = now()
        user.save()

        # Simulate sending OTP (replace with an SMS service in production)
        print(f"Your OTP is {user.otp}")

        return Response({"message": "OTP sent successfully"}, status=status.HTTP_200_OK)


# Verify OTP and Generate JWT
class VerifyOTPView(APIView):
    def post(self, request):
        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(mobile=serializer.validated_data['mobile'])
        user.otp = None
        user.otp_created_at = None
        user.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_type': 'seller' if user.is_seller else 'buyer',
        }, status=status.HTTP_200_OK)
    
# Register User (Buyers or Sellers)
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        return Response({
            'message': 'User registered successfully.',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)
    

# Buyer Dashboard
class BuyerDashboardView(APIView):
    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_buyer:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        buyer_data = BuyerProfileSerializer(request.user).data
        return Response({'dashboard_data': buyer_data}, status=status.HTTP_200_OK)


# Seller Dashboard
class SellerDashboardView(APIView):
    def get(self, request):
        if not request.user.is_authenticated or not request.user.is_seller:
            return Response({'detail': 'Unauthorized'}, status=status.HTTP_403_FORBIDDEN)

        seller_data = SellerProfileSerializer(request.user).data
        return Response({'dashboard_data': seller_data}, status=status.HTTP_200_OK)