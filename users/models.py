from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLES = [
        ("student", "학생"),
        ("professor", "교수"),
    ]
    nickname = models.CharField(max_length=30, unique=True)
    role = models.CharField(max_length=20, choices=ROLES, default="student")
    student_id = models.CharField(max_length=20, blank=True, null=True)  # 학번
    profile_image = models.ImageField(upload_to="profiles/", blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"