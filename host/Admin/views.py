import random
from django.shortcuts import render
import json
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
        executive_mail = request.GET.get('mail')
        if executive_mail:
            try:
                user = Executive.objects.get(mail=executive_mail)
                serializer = Executive_Serializer(user)
                return JsonResponse(serializer.data, safe=False)
            except Executive.DoesNotExist:
                return JsonResponse({'error': 'Administrador no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        Executives = Executive.objects.all()
        serializer=Executive_Serializer(Executives,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
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
    elif request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Distributor_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        user_id = request.GET.get('id')
        if user_id:
            try:
                user = Distributor.objects.get(id=user_id)
                request_data = JSONParser().parse(request)
                serializer = Distributor_Serializer(user, data=request_data)

                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Distributor.DoesNotExist:
                return JsonResponse({'error': 'Distribuidor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
def Domain_view(request, *args, **kwargs):
    if request.method == 'GET':
        domain_name = request.GET.get('name')
        if domain_name:
            try:
                domain = Domain.objects.filter(name__icontains=domain_name)
                serializer = Distributor_Serializer(domain)
                return JsonResponse(serializer.data, safe=False)
            except Domain.DoesNotExist:
                return JsonResponse({'error': 'Dominio no encontrado'}, status=status.HTTP_404_NOT_FOUND)       
        Domains = Domain.objects.all()
        serializer = Domain_Serializer(Domains, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Domain_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

def Process_view(request):
   
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            domain_name = data.get('domain_name')
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error al decodificar JSON'}, status=status.HTTP_400_BAD_REQUEST)

        if not domain_name:
            return JsonResponse({'error': 'Se requiere el nombre del dominio'}, status=status.HTTP_400_BAD_REQUEST)

        distributors = list(Distributor.objects.all())  # Convertimos a lista para poder modificarla

        if not distributors:
            return JsonResponse({'error': 'No hay distribuidores disponibles'}, status=status.HTTP_400_BAD_REQUEST)

        created_domains = []

        extensions = ['.co', '.eu', '.bz', '.org', '.com', '.pe']

        for extension in extensions:
            # Seleccionamos un distribuidor aleatorio y lo eliminamos de la lista
            selected_distributor = random.choice(distributors)
            domain_with_extension = domain_name + extension

            domain_data = {
                'name': domain_with_extension,
                'id_Distributor': selected_distributor.id,
                'available': random.choice([True, False]),
                'plataform': random.choice(['Unix', 'Windows']),
                'description': 'Descripción del dominio',
            }

            serializer = Domain_Serializer(data=domain_data)
            if serializer.is_valid():
                serializer.save()
                created_domains.append(serializer.data)

        return JsonResponse(created_domains, status=status.HTTP_200_OK, safe=False)

    return JsonResponse({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
