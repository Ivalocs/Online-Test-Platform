from django.urls import path
from . import views

urlpatterns = [
    path('recruiter-profile/<str:pk>/', views.recruiter_profile, name = 'recruiter-profile')
]