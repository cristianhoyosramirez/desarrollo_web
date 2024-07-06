# from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import *
from .serializer import *

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class=GenreSerializer
    queryset=Genre.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class=AuthorSerializer
    queryset=Author.objects.all()
    
class BookViewSet(viewsets.ModelViewSet):
    serializer_class=BookSerializer
    queryset=Book.objects.all()
    
class BookAuthorViewSet(viewsets.ModelViewSet):
    serializer_class=BookAutorSerializer
    queryset=BookAuthor.objects.all()
    