from random import choices
from django.db import models

# Create your models here.
class register_as(models.Model):
    REGISTER_TYPE = (
        ('Applicant', 'Applicant'),
        ('Recruiter', 'Recruiter')
    )
    who = models.CharField(max_length=100, choices=REGISTER_TYPE)