from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ValidationError
from .serializers import UserRegistrationSerializer
from .models import User

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
    
