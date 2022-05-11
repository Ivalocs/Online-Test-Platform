from django.contrib import admin

# Register your models here.
from .models import exam_details, exam_given

admin.site.register(exam_details)
admin.site.register(exam_given)
