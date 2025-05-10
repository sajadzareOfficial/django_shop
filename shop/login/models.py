from django.db import models
from django import forms
# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=12)
    def __str__(self):
        return self.name
    

    
