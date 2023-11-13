from django.db import models
from django.utils import timezone
# Create your models here.
class Employee(models.Model):
    OCCUPATION_TYPES = [
        ('Conectividad', 'Conectividad'),
        ('Pagos', 'Pagos'),
        ('Env', 'Env'),
        ('Privacidad', 'Privacidad'),
    ]
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    identification= models.CharField(max_length=200,default='',null=True,blank=True)
    address= models.CharField(max_length=100,default='',null=True,blank=True)
    mail= models.CharField(max_length=100,default='',null=True,blank=True)
    age= models.IntegerField(default=0)
    country= models.CharField(max_length=20,default='',null=True,blank=True)
    occupation= models.CharField(max_length=20,choices=OCCUPATION_TYPES,default='')
    salary= models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    h_entry= models.DateTimeField(default=timezone.now)
    affair= models.CharField(max_length=100,default='',null=True,blank=True)
    level= models.CharField(max_length=100,default='',null=True,blank=True)
    category= models.CharField(max_length=20,default='',null=True,blank=True)
    description= models.CharField(max_length=20,default='',null=True,blank=True)
    def __str__(self):
        return self.name
