import random
from django.shortcuts import render
import json
from django.http import HttpResponse
from django.utils import timezone
from xml.etree import ElementTree as ET
import traceback
from  Client.serializers import Plan_Serializer
from .models import Distributor, Domain,Executive
from Client.models import Plan, PlanClient
from .serializers import Distributor_Serializer
from .serializers import Domain_Serializer
from .serializers import Executive_Serializer
from django.http import JsonResponse, HttpResponseServerError
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import get_object_or_404


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
                serializer = Domain_Serializer(domain,many=True)
                return JsonResponse(serializer.data, safe=False)
            except Domain.DoesNotExist:
                return JsonResponse({'error': 'Dominios no encontrado'}, status=status.HTTP_404_NOT_FOUND)       
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
    if request.method == 'PUT':
        domain_id = request.GET.get('id')
        if domain_id:
            try:
                user = Domain.objects.get(id=domain_id)
                request_data = JSONParser().parse(request)
                serializer = Domain_Serializer(user, data=request_data)

                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_200_OK)
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except Domain.DoesNotExist:
                return JsonResponse({'error': 'Dominio no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({'error': 'Se requiere el parámetro "id" para la actualización'}, status=status.HTTP_400_BAD_REQUEST)

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

def search_Domain(request, *args, **kwargs):
    if request.method == 'GET':
        idClient = request.GET.get('idClient')

        if idClient:
            try:
                domains = Domain.objects.filter(id_Client=idClient)
                
                if domains.exists():
                    serializer = Domain_Serializer(domains, many=True)
                    return JsonResponse(serializer.data, safe=False)
                else:
                    return JsonResponse({'error': 'No se encontraron dominios para el cliente dado'}, status=status.HTTP_404_NOT_FOUND)

            except Domain.DoesNotExist:
                return JsonResponse({'error': 'Error al buscar dominios'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            # No se proporcionó un idClient, devolver todos los dominios
            domains = Domain.objects.all()
            serializer = Domain_Serializer(domains, many=True)
            return JsonResponse(serializer.data, safe=False)

def search_Plan(request, *args, **kwargs):
    if request.method == 'GET':
        idPlan = request.GET.get('idPlan')
        if idPlan:
            try:
                # Utiliza filter(id=idPlan) directamente para buscar por el id exacto
                plans = Plan.objects.filter(id=idPlan)

                if plans.exists():
                    serializer = Plan_Serializer(plans, many=True)
                    return JsonResponse(serializer.data, safe=False)
                else:
                    return JsonResponse({'error': 'No se encontraron planes para el plan dado'}, status=status.HTTP_404_NOT_FOUND)

            except Plan.DoesNotExist:
                return JsonResponse({'error': 'Error al buscar planes'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            # No se proporcionó un idPlan, devolver todos los planes
            plans = Plan.objects.all()
            serializer = Plan_Serializer(plans, many=True)
            return JsonResponse(serializer.data, safe=False)

#@csrf_exempt
def xml_report(request):
    if request.method == 'GET':
        # Paso 1: Traer todos los distribuidores asignados
        distributors = Distributor.objects.all()

        # Paso 2: Consulta en dominios registrados de los distribuidores en el mes actual
        current_month = datetime.now().month
        domains_in_month = Domain.objects.filter(
            id_Distributor__in=distributors,
            id_Plan__date_start__month=current_month
        )

        # Crear un diccionario para almacenar los archivos XML y las direcciones de correo electrónico
        xml_files = {}

        for distributor in distributors:
            xml_root = ET.Element("report")
            distributor_element = ET.SubElement(xml_root, "distributor")
            ET.SubElement(distributor_element, "name").text = distributor.name

            # Agregar los nombres de los dominios para este distribuidor
            domains_for_distributor = domains_in_month.filter(id_Distributor=distributor)
            for domain in domains_for_distributor:
                domain_element = ET.SubElement(distributor_element, "domain")
                ET.SubElement(domain_element, "name").text = domain.name

            # Convertir el árbol XML a una cadena
            xml_string = ET.tostring(xml_root, encoding='utf-8').decode('utf-8')

            # Agregar el archivo XML al diccionario
            xml_files[f"{distributor.name}_report.xml"] = xml_string

        # Enviar el correo electrónico a cada distribuidor con el archivo XML adjunto
        for distributor in distributors:
            xml_filename = f"{distributor.name}_report.xml"
            xml_string = xml_files.get(xml_filename, '')

            if xml_string:
                email = EmailMessage(
                    subject='Informe Mensual',
                    body='Adjunto encontrarás el informe mensual en formato XML.',
                    from_email=settings.EMAIL_HOST_USER,
                    to=[distributor.mail], 
                )
                email.attach(xml_filename, xml_string, 'application/xml')
                email.send()

        return HttpResponse("Correo(s) enviado(s) con éxito.")

