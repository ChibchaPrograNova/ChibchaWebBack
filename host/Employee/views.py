from django.shortcuts import render
from .models import Employee, Ticket
from .serializers import Employee_Serializer
from .serializers import Ticket_Serializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser

# Create your views here.
def Employee_view(request, *args, **kwargs):
    if request.method == 'GET':
        employee_id = request.GET.get('id')
        if employee_id:
            try:
                employee = Employee.objects.get(id=user_id)
                serializer = Client_Serializer(employee)
                return JsonResponse(serializer.data, safe=False)
            except Employee.DoesNotExist:
                return JsonResponse({'error': 'Empleado no encontrado'}, status=status.HTTP_404_NOT_FOUND)
        users = Employee.objects.all()
        serializer=Employee_Serializer(users,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Employee_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
def Ticket_view(request, *args, **kwargs):
    if request.method == 'GET':
        Tickets = Ticket.objects.all()
        serializer=Ticket_Serializer(Tickets,many=True)
        return JsonResponse(serializer.data,safe=False)
    if request.method == 'POST':
        request_data=JSONParser().parse(request)
        serializer=Ticket_Serializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=status.HTTP_200_OK)
        return JsonResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)