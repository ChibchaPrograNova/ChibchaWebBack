from .models import Card, Pay, Payment_Method
from rest_framework import serializers

class Card_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields= '__all__'

class Pay_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Pay
        fields= '__all__'

class Payment_Method_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Payment_Method
        fields= '__all__'
