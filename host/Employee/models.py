from django.db import models
from django.utils import timezone
# Create your models here.
OCCUPATION_TYPES = [
        ('Conectividad', 'Conectividad'),
        ('Pagos', 'Pagos'),
        ('Env', 'Env'),
        ('Privacidad', 'Privacidad'),
    ]

LEVEL_TYPES = [
    ('Basico', 'Basico'),
    ('Intermedio', 'Intermedio'),
    ('Critico', 'Critico'),
    ('Prioritario', 'Prioritario')

]
class Employee(models.Model):
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    identification= models.CharField(max_length=200,default='',null=True,blank=True)
    address= models.CharField(max_length=100,default='',null=True,blank=True)
    mail= models.CharField(max_length=100,default='',null=True,blank=True)
    password= models.CharField(max_length=200,default='',null=True,blank=True)
    age= models.IntegerField(default=0)
    country= models.CharField(max_length=20,default='',null=True,blank=True)
    occupation= models.CharField(max_length=20,choices=OCCUPATION_TYPES,default='')
    salary= models.IntegerField(default=0)
    activate= models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Ticket(models.Model):
    h_entry= models.DateTimeField(default=timezone.now)
    affair= models.CharField(max_length=100,default='',null=True,blank=True)
    level= models.CharField(max_length=100, choices=LEVEL_TYPES,null=True,blank=True)
    category= models.CharField(max_length=20,choices=OCCUPATION_TYPES,default='')
    description= models.TextField(default='',null=True,blank=True)
    def __str__(self):
        return self.affair
