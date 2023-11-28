from django.utils import timezone
from django.shortcuts import render
from .models import Card, Pay
from .serializers import Card_Serializer
from .serializers import Pay_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
import csv
from django.http import HttpResponse

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

def calculate_commission(distributor_type, amount):
    # Define las tasas de comisión según el tipo de distribuidor
    commission_rates = {
        'Básico': 0.1,
        'Premium': 0.15,
    }

    # Calcula la comisión
    commission_rate = commission_rates.get(distributor_type, 0)
    commission = amount * commission_rate

    return commission

def generate_commission_file(commissions):
    # Crea un archivo CSV con la información de las comisiones
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="commissions.csv"'

    writer = csv.writer(response)
    writer.writerow(['Distributor Name', 'Commission', 'Bank Account'])

    for commission in commissions:
        writer.writerow([commission['name'], commission['commission'], commission['bank_account']])

    return response

def calculate_and_generate_commissions(request):
    # Obtén los pagos realizados este mes
    current_month = timezone.now().month
    payments = Pay.objects.filter(date__month=current_month)

    # Inicializa una lista para almacenar la información de las comisiones
    commissions = []

    # Itera sobre los pagos y calcula las comisiones
    for payment in payments:
        distributor = payment.id_Distributor
        commission = calculate_commission(distributor.category, payment.amount)

        # Agrega la información de la comisión a la lista
        commissions.append({
            'name': distributor.name,
            'commission': commission,
            'bank_account': distributor.bank_account,
        })

    # Genera el archivo CSV y devuelve la respuesta
    return generate_commission_file(commissions)