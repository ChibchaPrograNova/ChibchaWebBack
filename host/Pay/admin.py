from django.contrib import admin
from .models import Pay, Card,Payment_Method

# Register your models here.
admin.site.register(Card)
admin.site.register(Pay)
admin.site.register(Payment_Method)
