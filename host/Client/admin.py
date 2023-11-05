from django.contrib import admin
from .models import Client, Plan, Plan_Client

# Register your models here.
admin.site.register(Plan_Client)
admin.site.register(Client)
admin.site.register(Plan)
