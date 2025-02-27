from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
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
