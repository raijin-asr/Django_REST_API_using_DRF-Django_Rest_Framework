from django.shortcuts import get_object_or_404, render
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
    
    #companies/updateCompany: deserialize the data and update the company
    @action(detail=False, methods=['put'])
    def updateCompany(self, request):
        company_id = request.data.get('company_id')
        company = get_object_or_404(Company, pk=company_id)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 'success',
                'message': 'Company updated successfully'
            }
            return JsonResponse(response_data)
        return JsonResponse(serializer.errors, status=400)

    #companies/deleteCompany: delete the company
    @action(detail=False, methods=['delete'])
    def deleteCompany(self, request):
        company_id = request.data.get('company_id')
        if company_id is None:
            response_data = {
                'status': 'error',
                'message': 'Company ID is required'
            }
            return JsonResponse(response_data, status=400)
        company = get_object_or_404(Company, pk=company_id)
        company.delete()
        response_data = {
            'status': 'success',
            'message': 'Company deleted successfully'
        }
        return JsonResponse(response_data)


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
    
    #employees/updateEmployee: deserialize the data and update the company
    @action(detail=False, methods=['put'])
    def updateEmployee(self, request):
        employee_id = request.data.get('employee_id')
        employee = get_object_or_404(Employee, pk=employee_id)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 'success',
                'message': 'Employee updated successfully'
            }
            return JsonResponse(response_data)
        return JsonResponse(serializer.errors, status=400)
    
    #employees/deleteEmployee: delete the company
    @action(detail=False, methods=['delete'])
    def deleteEmployee(self, request):
        employee_id = request.data.get('employee_id')
        if employee_id is None:
            response_data = {
                'status': 'error',
                'message': 'Employee ID is required'
            }
            return JsonResponse(response_data, status=400)
        employee = get_object_or_404(Employee, pk=employee_id)
        employee.delete()
        response_data = {
            'status': 'success',
            'message': 'Employee deleted successfully'
        }
        return JsonResponse(response_data)

