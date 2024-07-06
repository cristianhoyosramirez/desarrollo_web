#from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import * 
from .serializer import *

class CarViewSet(viewsets.ModelViewSet):
    serializer_class=CarSerializer
    queryset=Car.objects.all()
    
class PartViewSet(viewsets.ModelViewSet):
    serializer_class=PartSerializer
    queryset=Part.objects.all()
    
class displacementViewSet(viewsets.ModelViewSet):
    serializer_class=displacementSerializer
    queryset=displacement.objects.all()
    
class manufacturerViewSet(viewsets.ModelViewSet):
    serializer_class=manufacturerSerializer
    queryset=manufacturer.objects.all()
