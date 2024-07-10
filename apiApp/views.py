from django.shortcuts import render
from rest_framework import viewsets
from apiApp.models import Company, Employee
from apiApp.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
import io
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


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
        
    #companies/createCompany: deserialize the data and save the company
    @action(detail=False, methods=['post'])
    def createCompany(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 'success',
                'message': 'Company created successfully'
            }
            return JsonResponse(response_data)
        return JsonResponse(serializer.errors, status=400)
    
    # LONG PROCESS
    # def createCompany(self,request):
    #     if request.method == 'POST':

    #         #NO need of this below 3 lines as equest.data in Django Rest Framework (DRF) already provides you with the parsed data from the request body
    #         # data = request.data
    #         # stream = io.BytesIO(data) #convert the data to bytes
    #         # python_data=JSONParser().parse(stream) #parse the data to python data
            
    #         serializer = CompanySerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             response_data = {
    #                 'status': 'success', 
    #                 'message': 'Company created successfully'}
    #             return HttpResponse(JSONRenderer().render(response_data), content_type='application/json')
    #         return HttpResponse(JSONRenderer().render(serializer.errors), content_type='application/json', status=400)
    #     return HttpResponse(JSONRenderer().render({'error': 'Invalid request'}), content_type='application/json', status=400)

#Employee Views
class EmployeeViewSet(viewsets.ModelViewSet): 
    queryset= Employee.objects.all() 
    serializer_class= EmployeeSerializer

    #employees/createEmployee: deserialize the data and save the company
    @action(detail=False, methods=['post'])
    def createEmployee(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 'success',
                'message': 'New Employee created successfully'
            }
            return JsonResponse(response_data)
        return JsonResponse(serializer.errors, status=400)

