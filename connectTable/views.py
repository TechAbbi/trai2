from django.shortcuts import render
from .models import ModelA, ModelB, ConnectingModel
from .serializers import ModelASerializer, ModelBSerializer, ConnectingModelSerializer

from rest_framework import generics
from rest_framework.response import Response


# Create your views here.

class ConnectTableListView(generics.ListCreateAPIView):
    queryset = ConnectingModel.objects.all()
    serializer_class = ConnectingModelSerializer
