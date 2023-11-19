from django.db import models
from django.utils import timezone


class Client(models.Model):
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    identification= models.CharField(max_length=200,default='',null=True,blank=True)
    address= models.CharField(max_length=100,default='',null=True,blank=True)
    mail= models.CharField(max_length=100,default='',null=True,blank=True)
    age= models.IntegerField(default=0)
    country= models.CharField(max_length=20,default='',null=True,blank=True)
    plans = models.ManyToManyField('Plan', through='PlanClient', related_name='clients', blank=True)

    def __str__(self):
        return self.name

class Plan(models.Model):
    PLAN_TYPES = [
        ('Plata', 'Plata'),
        ('Platino', 'Platino'),
        ('Oro', 'Oro'),
    ]
    date_start= models.DateTimeField(default=timezone.now, null=True, blank=True)
    date_end= models.DateTimeField(default=timezone.now, null=True, blank=True)
    category= models.CharField(max_length=100,choices=PLAN_TYPES,default='')
    def __str__(self):
        return self.category
    
class PlanClient(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.plan} - {self.client}"
        