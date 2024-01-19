from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import Student, Exam
from .serializers import StudentSerializer, ExamSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["first_name", "score"]
    # filter_backends = [filters.SearchFilter]
    filter_backends = [filters.OrderingFilter]
    search_fields = ["=first_name"]
    permission_classes = (IsAuthenticated,)


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date"]


class StudentOnExamDateAPIView(generics.ListAPIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        # Get the exam date from the URL parameters
        exam_date = self.kwargs.get('exam_date')

        # Filter the Exam model to get all exams on the specified date
        exams_on_date = Exam.objects.filter(date=exam_date)

        # Get the related students for all exams on the specified date
        students_on_date = Student.objects.filter(exams__in=exams_on_date)

        return students_on_date



# class StudentList(generics.ListAPIView, generics.CreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#

"""
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class StudentDetails(APIView):
    def get_object(self, pk):
        try:
            student = Student.objects.get(pk=pk)
            return student
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk=pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""
