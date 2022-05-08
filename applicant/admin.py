from django.contrib import admin

# Register your models here.

from .models import applicant_profile_model

admin.site.register(applicant_profile_model)