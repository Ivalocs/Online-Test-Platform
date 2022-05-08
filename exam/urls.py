from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_exam, name = "register-exam"),
    path('take_test/<str:pk>/', views.take_test, name = "take-test"),
    path('list/', views.list_tests, name = "list-tests"),
    path('report/<str:pk>/', views.report, name = "report"),
]

