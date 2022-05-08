from django.urls import path
from . import views

urlpatterns = [
    path('applicant-profile/<str:pk>/', views.applicant_profile, name = 'applicant-profile')
]

