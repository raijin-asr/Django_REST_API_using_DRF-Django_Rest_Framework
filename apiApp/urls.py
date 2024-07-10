from django.contrib import admin
from django.urls import path, include
from apiApp.views import CompanyViewSet, EmployeeViewSet
from rest_framework.routers import DefaultRouter

#viewset is a class that provides the CRUD operations
router = DefaultRouter() #create a router object to register the viewset
router.register(r'companies', CompanyViewSet) #register the viewset with the router (r is used to specify the raw string)
router.register(r'employees', EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)), #include the urls of the router
    # path('createCompany/', CompanyViewSet.createCompany, name='createCompany') # no needed as we are using action decorator to create custom actions
]