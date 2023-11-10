from .models import Distributor, Domain
from rest_framework import serializers

class Distributor_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Distributor
        fields= '__all__'

class Domain_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Domain
        fields= '__all__'
