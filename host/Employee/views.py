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
        serializer=Ticket_Serializer(Tickets,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method == 'POST':
        client_id = request.GET.get('id')
        if client_id:
            request_data = JSONParser().parse(request)
            user = Client.objects.filter(
                id__in=[client_id]
            ).first()  # Usar .first() para obtener el primer objeto del conjunto de consultas
            if user:
                email = EmailMessage(
                    subject='Respuesta a su solicitud de ayuda',
                    body=request_data['solucion'],
                    from_email=settings.EMAIL_HOST_USER,
                    to=[user.mail], 
                )
                email.send()
            else:
                # Manejar el caso donde no se encuentra un cliente con el ID proporcionado
                return JsonResponse({'error': 'Cliente no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        # Mover esta parte fuera del bloque else para asegurarse de que se ejecute siempre
        request_data = JSONParser().parse(request)
        serializer = Ticket_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
