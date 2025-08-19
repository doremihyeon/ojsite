from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Django 기본 User 필드: username, email, password 등
    nickname = models.CharField(max_length=30, unique=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return self.username