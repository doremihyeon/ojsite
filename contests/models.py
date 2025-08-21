from django.db import models
from django.conf import settings
from problems.models import Problem

class Contest(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    problems = models.ManyToManyField(Problem, related_name="contests")  # 대회 문제들
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class ContestSubmission(models.Model):
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE)
    submission = models.ForeignKey("submissions.Submission", on_delete=models.CASCADE)
    ranked = models.BooleanField(default=False)  # 점수 반영 여부