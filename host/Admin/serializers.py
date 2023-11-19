from .models import Distributor, Domain,Executive
from rest_framework import serializers

class Distributor_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Distributor
        fields= '__all__'

class Domain_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Domain
        fields= '__all__'

class Executive_Serializer(serializers.ModelSerializer):
    class Meta:
        model= Executive
        fields= '__all__'
