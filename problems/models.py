from django.db import models
from django.conf import settings

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=20,
        choices=[("easy", "쉬움"), ("medium", "보통"), ("hard", "어려움")],
        default="medium"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # 문제 출제자(학생/교수)

    def __str__(self):
        return self.title