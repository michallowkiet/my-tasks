from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


# Create your models here.
class CustomUser(AbstractUser):
    objects = CustomUserManager()
    USER_ROLES = (
        ("user", "User"),
        ("admin", "Admin"),
    )
    USERNAME_FIELD = "email"
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=255, choices=USER_ROLES, default="user")
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
