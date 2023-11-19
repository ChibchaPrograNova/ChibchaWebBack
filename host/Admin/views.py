from django.shortcuts import render
from .models import Distributor, Domain
from .serializers import Distributor_Serializer
from .serializers import Domain_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser


# Create your views here.
def Distributor_view(request, *args, **kwargs):
    if request.method == 'GET':
        users = Distributor.objects.all()
        serializer=Distributor_Serializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Distributor_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def Domain_view(request, *args, **kwargs):
    if request.method == 'GET':
        Domains = Domain.objects.all()
        serializer=Domain_Serializer(Domains,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Domain_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)