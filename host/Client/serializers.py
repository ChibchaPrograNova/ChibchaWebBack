from .models import Client, Plan, Plan_Client
from rest_framework import serializers

class Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Client
        fields= '__all__'

class Plan_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Plan
        fields= '__all__'

class Plan_Client_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Plan_Client
        fields= '__all__'
