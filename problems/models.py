from django.db import models

class Problem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=20,
        choices=[("easy", "쉬움"), ("medium", "보통"), ("hard", "어려움")],
        default="medium"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title