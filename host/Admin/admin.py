from django.contrib import admin
from .models import Distributor, Domain,Executive


# Register your models here.
admin.site.register(Distributor)
admin.site.register(Domain)
admin.site.register(Executive)