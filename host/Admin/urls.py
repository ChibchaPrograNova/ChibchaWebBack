from .views import Distributor_view,Domain_view 
from .views import Executive_view, Process_view,search_Domain,search_Plan
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('Distributors/', csrf_exempt(Distributor_view)),
             path('Domain/',csrf_exempt(Domain_view)),
             path('Executive/',csrf_exempt(Executive_view)),
             path('Process/',csrf_exempt(Process_view)),
             path('Search/',csrf_exempt(search_Domain)),
             path('Search/',csrf_exempt(search_Plan)),]
