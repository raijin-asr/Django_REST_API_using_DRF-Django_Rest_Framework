from django.contrib import admin
from django.urls import path, include
from apiApp.views import CompanyViewSet
from rest_framework import routers

router = routers.DefaultRouter() #create a router object to register the viewset
router.register(r'companies', CompanyViewSet) #register the viewset with the router (r is used to specify the raw string)

urlpatterns = [
    path('', include(router.urls)), #include the urls of the router
]