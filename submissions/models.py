from django.db import models
from django.conf import settings
from problems.models import Problem

class Submission(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    code = models.TextField()
    result = models.CharField(
        max_length=50,
        choices=[
            ("Accepted", "정답"),
            ("Wrong Answer", "오답"),
            ("Runtime Error", "실행 오류"),
            ("Time Limit Exceeded", "시간 초과"),
        ],
        default="Wrong Answer"
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.problem.title} ({self.result})"