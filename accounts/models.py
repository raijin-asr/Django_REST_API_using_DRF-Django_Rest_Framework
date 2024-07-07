from django.db import models
from django.contrib.auth.models import AbstractUser #import the AbstractUser class

# Create your models here.
class CustomUser(AbstractUser): #inherit the AbstractUser class
    username= models.CharField(max_length=50, unique=True) #username field
    email= models.EmailField(unique=True) #email field
    password= models.CharField(max_length=100) #password field
    isActive= models.BooleanField(default=True) #is active field

    def __str__(self):
        return self.username #return the username