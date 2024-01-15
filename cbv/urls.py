from django.urls import path
from . import views
urlpatterns = [
    path("", views.StudentList.as_view(), name="student_list"),
    path("<int:pk>/", views.StudentDetails.as_view(), name="Student_details")
]