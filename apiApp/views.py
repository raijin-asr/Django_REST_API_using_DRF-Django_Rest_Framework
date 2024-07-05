from django.shortcuts import render
from rest_framework import viewsets
from apiApp.models import Company
from apiApp.serializers import CompanySerializer

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet): # ModelViewSet is a class that provides the CRUD operations
    queryset= Company.objects.all() #queryset is a variable that holds all the objects of the model
    serializer_class= CompanySerializer #serializer_class is a variable that holds the serializer class
    