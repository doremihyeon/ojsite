from django.db import models
from django.conf import settings
from problems.models import Problem
from submissions.models import Submission

class Assignment(models.Model):
    title = models.CharField(max_length=200)                    # 과제 제목
    description = models.TextField(blank=True, null=True)       # 과제 설명
    start_time = models.DateTimeField()                         # 과제 시작 시간
    end_time = models.DateTimeField()                           # 과제 마감 시간
    problems = models.ManyToManyField(Problem, related_name="assignments")  # 포함된 문제들
    created_by = models.ForeignKey(                             # 교수님
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"role": "professor"}
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.submission.user.username} - {self.assignment.title}"