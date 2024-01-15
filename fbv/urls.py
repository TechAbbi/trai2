from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("<int:pk>/", views.student_details, name="details"),
]
