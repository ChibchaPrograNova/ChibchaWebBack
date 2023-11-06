from django.contrib import admin
from .models import Ticket, Employee

# Register your models here.
admin.site.register(Employee)
admin.site.register(Ticket)