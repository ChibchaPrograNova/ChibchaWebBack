import json
from django.shortcuts import render
from .models import Employee, Ticket
from .serializers import Employee_Serializer
from .serializers import Ticket_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.core.mail import EmailMessage
from django.conf import settings
from Client.models import Client

# Create your views here.
def Employee_view(request, *args, **kwargs):
    if request.method == 'GET':
        employee_id = request.GET.get('id')
        if employee_id:
            try:
                employee = Employee.objects.get(id=employee_id)
                serializer = Employee_Serializer(employee)
                return JsonResponse(serializer.data, safe=False)
            except Employee.DoesNotExist:
                return JsonResponse({'error': 'Empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        user_mail = request.GET.get('mail')
        if user_mail:
            try:
                user = Employee.objects.get(mail=user_mail)
                serializer = Employee_Serializer(user)
                return JsonResponse(serializer.data, safe=False)
            except Employee.DoesNotExist:
                return JsonResponse({'error': 'Empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)        
        users = Employee.objects.all()
        serializer = Employee_Serializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Employee_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PUT':
        user_id = request.GET.get('id')
        if user_id:
            try:
                user = Employee.objects.get(id=user_id)
                request_data = JSONParser().parse(request)
                serializer = Employee_Serializer(user, data=request_data)

                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Employee.DoesNotExist:
                return JsonResponse({'error': 'UEmpleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
def Ticket_view(request, *args, **kwargs):
    if request.method == 'GET':
        Tickets = Ticket.objects.all()
        serializer = Ticket_Serializer(Tickets, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        try:
            # Utilizamos JSONParser desde rest_framework
            request_data = JSONParser().parse(request)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Error de formato JSON en la solicitud'}, status=status.HTTP_400_BAD_REQUEST)

        client_id = request_data.get('client')
        solucion = request_data.get('solucion')

        if not all([client_id, solucion]):
            return JsonResponse({'error': 'Campos "client" y "solucion" son requeridos'}, status=status.HTTP_400_BAD_REQUEST)

        user = Client.objects.filter(id=client_id).first()
        if not user:
            return JsonResponse({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        request_data['client'] = user.id

        serializer = Ticket_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()

            # Envía un correo electrónico después de guardar el ticket
            email = EmailMessage(
                subject='Respuesta a su solicitud de ayuda',
                body=solucion,
                from_email=settings.EMAIL_HOST_USER,
                to=[user.mail],
            )
            email.send()

            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        return JsonResponse({'error': 'Método no permitido'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)