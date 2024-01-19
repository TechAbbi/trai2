from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register("students", views.StudentViewSet)
router.register("exam", views.ExamViewSet)



urlpatterns = [
    # path("", views.StudentList.as_view(), name="student_list"),
    # path("<int:pk>/", views.StudentDetails.as_view(), name="Student_details"),
    path("api/", include(router.urls)),
    path('students/on_exam_date/<str:exam_date>/', views.StudentOnExamDateAPIView.as_view(),
         name='student-on-exam-date'),
    path("api_auth_token/", obtain_auth_token, name="api_auth_token")
]
