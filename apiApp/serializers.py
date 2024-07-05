from rest_framework import serializers
from apiApp.models import Company

#create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id= serializers.ReadOnlyField() #this field is read only
    class Meta: #this is a class that holds metadata
        model= Company
        fields="__all__" #for all fields

        