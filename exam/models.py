from django.db import models
from django.contrib.auth.models import User
from recruiter.models import recruiter_profile_model
import uuid

class exam_details(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    created_by = models.ForeignKey(recruiter_profile_model, on_delete=models.CASCADE, null=True)
    questions = models.TextField(blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)

class exam_given(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    exam = models.CharField(max_length=200, blank=True, null=True)
    correct = models.IntegerField(blank = True, null = True)
    incorrect = models.IntegerField(blank = True, null = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.exam)
