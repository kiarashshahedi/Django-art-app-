from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
import random
from django.utils.timezone import now, timedelta

# My Custom Usermanager
class UserManager(BaseUserManager):
    def create_user(self, mobile, is_seller=False, **extra_fields):
        if not mobile:
            raise ValueError("Mobile number is required")
        user = self.model(mobile=mobile, is_seller=is_seller, **extra_fields)
        user.set_password(None)  # OTP-based login
        user.save(using=self._db)
        return user

# Users
class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    mobile = models.CharField(max_length=15, unique=True, blank=False, null=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'mobile'

