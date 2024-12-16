from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserRegistrationView, GenerateOTPView, VerifyOTPView, BuyerDashboardView, SellerDashboardView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    # otp
    path('generate-otp/', GenerateOTPView.as_view(), name='generate-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    # token
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # dashboard
    path('buyer/dashboard/', BuyerDashboardView.as_view(), name='buyer_dashboard'),
    path('seller/dashboard/', SellerDashboardView.as_view(), name='seller_dashboard'),


]
