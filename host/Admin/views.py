import random
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

def Process_view(request, ):
    if request.method == 'POST':
        # Paso 1: Recibir el nombre del dominio desde la solicitud
        domain_name = request.POST.get('domain_name')

        if not domain_name:
            return JsonResponse({'error': 'Se requiere el nombre del dominio'}, status=status.HTTP_400_BAD_REQUEST)

        # Paso 2: Consultar todos los distribuidores
        distributors = Distributor.objects.all()

        if not distributors.exists():
            return JsonResponse({'error': 'No hay distribuidores disponibles'}, status=status.HTTP_400_BAD_REQUEST)

        # Paso 3: Asociar aleatoriamente el dominio a un distribuidor
        selected_distributor = random.choice(distributors)

        # Paso 4: Crear un array con propiedades adicionales para el dominio
        additional_properties = {
            'property1': 'value1',
            'property2': 'value2',
            # Agrega más propiedades según sea necesario
        }

        # Paso 5: Agregar extensiones al nombre del dominio y guardar en la base de datos
        extensions = ['.co', '.eu', '.bz', '.org', '.com', '.pe']
        created_domains = []

        for extension in extensions:
            domain_with_extension = domain_name + extension

            # Paso 6: Guardar el dominio en la base de datos
            domain_data = {
                'name': domain_with_extension,
                'id_Distributor': selected_distributor.id,
                'available': True,  # Puedes ajustar esto según tus necesidades
                'plataform': 'Windows',  # Puedes ajustar esto según tus necesidades
                'description': 'Descripción del dominio',  # Puedes ajustar esto según tus necesidades
                **additional_properties,  # Agrega propiedades adicionales
            }

            serializer = Domain_Serializer(data=domain_data)
            if serializer.is_valid():
                serializer.save()
                created_domains.append(serializer.data)

        return JsonResponse(created_domains, status=status.HTTP_200_OK, safe=False)

    return JsonResponse({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)