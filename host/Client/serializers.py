from .models import Client, Plan
from rest_framework import serializers

class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= '__all__'

class Plan_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Plan
        fields= '__all__'


