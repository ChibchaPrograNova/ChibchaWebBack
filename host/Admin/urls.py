from .views import Distributor_view,Domain_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('Distributors/', csrf_exempt(Distributor_view)),
             path('Domain/',csrf_exempt(Domain_view)),
             ]
