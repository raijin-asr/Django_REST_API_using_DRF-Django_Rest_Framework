from django.db import models

# Create your models here.
class Company(models.Model):
    company_id= models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    location= models.CharField(max_length=100)
    ceo= models.CharField(max_length=100)
    company_type= models.CharField(
        max_length=100, 
        choices=(
            ('IT','IT'),
            ('Non IT','Non IT'),
    ))
    added_date= models.DateTimeField(auto_now=True)
    active= models.BooleanField(default=True)

    def __str__(self):
        return self.name + '(' + self.location +')' #return the name,location of the company
    
#Employee model
class Employee(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    address= models.CharField(max_length=100)
    phone= models.CharField(max_length=10)
    designation= models.CharField(
        max_length=100,
        choices=(
            ('Developer','Developer'),
            ('Tester','Tester'),
            ('Manager','Manager'),
            ('HR','HR'),
    ))
    company= models.ForeignKey(Company, on_delete=models.CASCADE) #foreign key to company model (one to many relationship)
