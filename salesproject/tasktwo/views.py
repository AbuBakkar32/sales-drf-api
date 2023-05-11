from django.shortcuts import render
from rest_framework import generics
from .models import SalesModel
from .serializers import SalesSerializer


# Create your views here.
class TaskTwoListCreateView(generics.ListCreateAPIView):
    queryset = SalesModel.objects.all()
    serializer_class = SalesSerializer


class TaskTwoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesModel.objects.all()
    serializer_class = SalesSerializer
