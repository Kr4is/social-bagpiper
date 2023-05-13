from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_photo = models.ImageField(default="default.jpg", upload_to="profile_images")
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.username}"
