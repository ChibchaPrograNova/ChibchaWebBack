from django.db import models
from Client.models import Client
from django.utils import timezone


# Create your models here.
class Card(models.Model):
    id_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    type= models.CharField(max_length=200,default='',null=True,blank=True)
    h_entry= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Pay(models.Model):
    id_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_Card = models.ForeignKey(Card, on_delete=models.CASCADE)
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    amount= models.IntegerField(default=0)
    date= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
class Payment_Method(models.Model):
    id_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    type= models.CharField(max_length=200,default='',null=True,blank=True)
    method= models.IntegerField(default=0)

    def __str__(self):
        return self.name