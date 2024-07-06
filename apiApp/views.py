from django.shortcuts import render
from rest_framework import viewsets
from apiApp.models import Company, Employee
from apiApp.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your Company views here.
class CompanyViewSet(viewsets.ModelViewSet): # ModelViewSet is a class that provides the CRUD operations
    queryset= Company.objects.all() #queryset is a variable that holds all the objects of the model
    serializer_class= CompanySerializer #serializer_class is a variable that holds the serializer class
    
    #action decorator is used to create custom actions
    #companies/{id}/employees
    @action(detail=True, methods=['get']) # detail=True means that the action is for a single object
    def employees(self, request, pk=None):
        # print("Company ID: ", pk) #print the company id
        try:
            company=Company.objects.get(pk=pk) #get the company object with the company id
            emps=Employee.objects.filter(company=company) #get all the employees of the company
            emps_serializer=EmployeeSerializer(emps, many=True, context={'request':request}) #serialize the employees
            return Response(emps_serializer.data) #return the serialized data

        # except Company.DoesNotExist:
        except Exception as e:
            print(e)
            return Response({'error':'Company not found'}, status=404)
        
#Employee Views
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class= EmployeeSerializer