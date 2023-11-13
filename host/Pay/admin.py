from django.contrib import admin
from .models import Pay, Card

# Register your models here.
admin.site.register(Card)
admin.site.register(Pay)