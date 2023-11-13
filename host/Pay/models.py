from django.db import models
from Client.models import Client
from django.utils import timezone


# Create your models here.
class Card(models.Model):
    id_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    number= models.CharField(max_length=200,default='',null=True,blank=True)
    type= models.CharField(max_length=200,default='',null=True,blank=True)
    d_expiration= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.number

class Pay(models.Model):
    PAY_TYPES = [
        ('Mensual', 'Mensual'),
        ('Trimestral', 'Trimestral'),
        ('Semestral', 'Semestral'),
        ('Anual', 'Anual'),
    ]
    id_Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_Card = models.ForeignKey(Card, on_delete=models.CASCADE)
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    amount= models.IntegerField(default=0)
    type= models.CharField(max_length=200,choices=PAY_TYPES,default='')
    date= models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.name
    