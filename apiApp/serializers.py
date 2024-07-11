from rest_framework import serializers
from apiApp.models import Company, Employee

#create serializers here
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id= serializers.ReadOnlyField() #this field is read only
    class Meta: #this is a class that holds metadata
        model= Company
        fields="__all__" #for all fields

        def update(self, instance, validated_data):
            instance.company_id = validated_data.get('company_id', instance.company_id)
            instance.name = validated_data.get('name', instance.name)
            instance.location = validated_data.get('location', instance.location)
            instance.ceo = validated_data.get('ceo', instance.ceo)
            instance.company_type = validated_data.get('company_type', instance.company_type)
            instance.added_date = validated_data.get('added_date', instance.added_date)
            instance.active = validated_data.get('active', instance.active)
            instance.save()
            return instance

#create employee serializer
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    employee_id= serializers.ReadOnlyField() #this field is read only
    class Meta:
        model= Employee
        fields="__all__" #for all fields

        def update(self, instance, validated_data):
            instance.employee_id = validated_data.get('employee_id', instance.employee_id)
            instance.name = validated_data.get('name', instance.name)
            instance.email = validated_data.get('email', instance.email)
            instance.address = validated_data.get('address', instance.address)
            instance.phone = validated_data.get('phone', instance.phone)
            instance.designation = validated_data.get('designation', instance.designation)
            instance.company = validated_data.get('company', instance.company)
            instance.save()
            return instance