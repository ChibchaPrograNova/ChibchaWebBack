from django.utils import timezone  # Cambia esta línea
from django.db import models
from Client.models import Client,Plan

# Create your models here.

class Executive(models.Model):
    mail= models.CharField(max_length=200,default='',null=True,blank=True)
    password= models.CharField(max_length=200,default='',null=True,blank=True)
    def __str__(self):
        return self.mail
    
class Distributor(models.Model):
    DISTRIBUTOR_CATEGORY = [
        ('Básico', 'Básico'),
        ('Premium', 'Premium'),
    ]
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    nit= models.CharField(max_length=200,default='',null=True,blank=True)
    address= models.CharField(max_length=100,default='',null=True,blank=True)
    mail= models.CharField(max_length=100,default='',null=True,blank=True)
    q_domains= models.IntegerField(default=0)
    category= models.CharField(max_length=20,choices=DISTRIBUTOR_CATEGORY,default='')
    bank_account= models.CharField(max_length=20,default='',null=True,blank=True)
    activate= models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
class Domain(models.Model):
    PLATAFORM_TYPE = [
        ('Windows', 'Windows'),
        ('Unix', 'Unix'),
    ]
    id_Client = models.ForeignKey(Client, on_delete=models.CASCADE,null=True,blank=True)
    id_Plan = models.ForeignKey(Plan, on_delete=models.CASCADE,null=True,blank=True)
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    id_Distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)    
    available= models.BooleanField(default=True)
    plataform= models.CharField(max_length=100,choices=PLATAFORM_TYPE,default='')
    description = models.TextField(default='', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)  # Corregir esta línea

    def __str__(self):
        return self.name