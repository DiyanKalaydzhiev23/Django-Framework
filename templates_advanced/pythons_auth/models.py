from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    description = models.TextField()
    website = models.CharField(
        max_length=30
    )
    profile_image = models.ImageField(
        upload_to="profiles/"
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
