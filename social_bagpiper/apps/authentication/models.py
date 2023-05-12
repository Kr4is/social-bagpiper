from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    profile_photo = models.ImageField(default="default.png", upload_to="profile_images")

    def __str__(self):
        return f"{self.username}"
