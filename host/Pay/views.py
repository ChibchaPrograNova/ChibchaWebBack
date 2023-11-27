from django.shortcuts import render
from .models import Card, Pay
from .serializers import Card_Serializer
from .serializers import Pay_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from Client.models import Client


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

def calculate_commissions(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        
        try:
            client_id = request_data['id_Client']
            client = Client.objects.get(pk=client_id)
            distributor = client.distributor_set.first()
            
            if distributor:
                commission_percentage = 0.10 if distributor.category == 'Básico' else 0.15
                commission = request_data['amount'] * commission_percentage
                
                # Aquí puedes implementar la lógica específica para separar las comisiones
                # En este ejemplo, simplemente se imprime la comisión calculada
                print(f"Comisión total: {commission}")
                print(f"Comisión para {distributor.name}: {commission}")
                
                return JsonResponse({'message': 'Comisiones calculadas correctamente.'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error': 'El cliente no tiene un distribuidor asociado.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return JsonResponse({'error': 'Método no permitido.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)