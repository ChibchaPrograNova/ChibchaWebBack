from .models import Employee, Ticket
from rest_framework import serializers

class Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields= '__all__'

class Ticket_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Ticket
        fields= '__all__'
