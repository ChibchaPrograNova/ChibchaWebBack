from django.db import models

# Create your models here.
class Distributor(models.Model):
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    nit= models.CharField(max_length=200,default='',null=True,blank=True)
    address= models.CharField(max_length=100,default='',null=True,blank=True)
    mail= models.CharField(max_length=100,default='',null=True,blank=True)
    q_domains= models.IntegerField(max_length=3,default='',null=True,blank=True)
    category= models.CharField(max_length=20,default='',null=True,blank=True)
    bank_account= models.CharField(max_length=100,default='',null=True,blank=True)
    def __str__(self):
        return self.name
    
class Domain(models.Model):
    name= models.CharField(max_length=200,default='',null=True,blank=True)
    id_Distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    available= models.BooleanField(default=True)
    plataform= models.CharField(max_length=200,default='',null=True,blank=True)
    def __str__(self):
        return self.name