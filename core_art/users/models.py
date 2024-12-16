from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    mobile = models.CharField(max_length=15, unique=True, blank=False, null=False)
    REQUIRED_FIELDS = ['email', 'mobile']
