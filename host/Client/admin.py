from django.contrib import admin
from .models import Client, Plan,PlanClient

# Register your models here.
admin.site.register(Client)
admin.site.register(Plan)
admin.site.register(PlanClient)

