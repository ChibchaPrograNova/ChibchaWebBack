from .models import Card, Pay
from rest_framework import serializers

class Card_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Card
        fields= '__all__'

class Pay_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Pay
        fields= '__all__'

