from django.shortcuts import render
from .models import Distributor, Domain,Executive
from .serializers import Distributor_Serializer
from .serializers import Domain_Serializer
from .serializers import Executive_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser


# Create your views here.
def Executive_view(request, *args, **kwargs):
    if request.method == 'GET':
        Executives = Executive.objects.all()
        serializer=Executive_Serializer(Executives,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Executive_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def Distributor_view(request, *args, **kwargs):
    if request.method == 'GET':
        user_id = request.GET.get('id')
        if user_id:
            try:
                user = Distributor.objects.get(id=user_id)
                serializer = Distributor_Serializer(user)
                return JsonResponse(serializer.data, safe=False)
            except Distributor.DoesNotExist:
                return JsonResponse({'error': 'Distribuidor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        user_mail = request.GET.get('mail')
        if user_mail:
            try:
                user = Distributor.objects.get(mail=user_mail)
                serializer = Distributor_Serializer(user)
                return JsonResponse(serializer.data, safe=False)
            except Distributor.DoesNotExist:
                return JsonResponse({'error': 'Distribuidor no encontrado'}, status=status.HTTP_404_NOT_FOUND)        
        users = Distributor.objects.all()
        serializer = Distributor_Serializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

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