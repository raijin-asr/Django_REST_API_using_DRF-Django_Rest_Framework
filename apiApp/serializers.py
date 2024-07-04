from rest_framework import serializers
from apiApp.models import Company

#create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta: #this is a class that holds metadata
        model= Company
        field: "__all__" #for all fields

        