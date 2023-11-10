from django.shortcuts import render
from .models import Card, Pay, Payment_Method
from .serializers import Card_Serializer
from .serializers import Pay_Serializer,Payment_Method_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.
def Card_view(request, *args, **kwargs):
    if request.method == 'GET':
        users = Card.objects.all()
        serializer=Card_Serializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Card_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def Pay_view(request, *args, **kwargs):
    if request.method == 'GET':
        Pays = Pay.objects.all()
        serializer=Pay_Serializer(Pays,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Pay_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def Payment_Method_view(request, *args, **kwargs):
    if request.method == 'GET':
        Payment_Methods = Payment_Method.objects.all()
        serializer=Payment_Method_Serializer(Payment_Methods,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Payment_Method_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)