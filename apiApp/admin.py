from django.contrib import admin
from apiApp.models import Company, Employee

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display= ('company_id', 'name','ceo', 'location','company_type') #display these fields in the admin panel
    search_fields= ('name','ceo') #search these fields in the admin panel
    list_filter= ('company_type',) #filter by company type

class EmployeeAdmin(admin.ModelAdmin):
    list_display= ('name','phone', 'designation','company') #display these fields in the admin panel
    search_fields= ('name','designation') #search these fields in the admin panel
    list_filter= ('designation',) #filter by designation
    
admin.site.register(Company, CompanyAdmin) #register the company model
admin.site.register(Employee,EmployeeAdmin) #register the employee model
