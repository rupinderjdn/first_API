from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api import models
from api import serialize
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
) 
from django.views.generic import ListView
# Create your views here.
class CarsView(ListView):
    model=models.Car
    template_name='data.html'
    context_object_name="cars"
class CarListView(ListAPIView):
    queryset=models.Car.objects.all()
    serializer_class=serialize.CarSerializer
class CarDetailView(RetrieveAPIView):
    queryset=models.Car.objects.all()
    serializer_class=serialize.CarSerializer
class CarUpdateView(RetrieveUpdateAPIView):
    queryset=models.Car.objects.all()
    serializer_class=serialize.CarSerializer
class CarDeleteView(RetrieveDestroyAPIView):
    queryset=models.Car.objects.all()
    serializer_class=serialize.CarSerializer
