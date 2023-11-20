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
'''
def Process_view(request,*args, **kwargs):
    if request.method == 'POST':
        nombre = request.GET.get('nombre')

        # Paso 1: Consultar todos los distribuidores
        distribuidores_endpoint = '/Admins/Distributors/'
        response_distribuidores = requests.get(distribuidores_endpoint)

        if response_distribuidores.status_code != 200:
            return JsonResponse({'error': 'Error al obtener los distribuidores'}, status=500)

        distribuidores = response_distribuidores.json()

        # Paso 2: Crear un array con las extensiones especificadas
        extensiones = ['.co', '.eu', '.bz', '.org', '.com', '.pe']

        # Mezclar los dos arrays
        distribuidores_extensiones = [(distribuidor, extension) for distribuidor in distribuidores for extension in extensiones]
        random.shuffle(distribuidores_extensiones)

        # Paso 3: Crear otro array con propiedades adicionales
        resultado_final = []

        for distribuidor, extension in distribuidores_extensiones:
            resultado_final.append({
                'nombre': nombre,
                'distribuidor': distribuidor,
                'extension': extension,
                'disponibilidad': random.uniform(0, 1),
                'plataforma': random.choice(['Unix', 'Windows']),
            })

        return JsonResponse({'resultados': resultado_final}, status=200)

    return JsonResponse({'error': 'Método no permitido'}, status=405)
'''