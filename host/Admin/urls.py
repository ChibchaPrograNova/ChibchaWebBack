from .views import Distributor_view,Domain_view 
from .views import Executive_view, Process_view
from .views import search_Domain,search_Plan,distributor_data_for_xml
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('Distributors/', csrf_exempt(Distributor_view)),
             path('Domain/',csrf_exempt(Domain_view)),
             path('Executive/',csrf_exempt(Executive_view)),
             path('Process/',csrf_exempt(Process_view)),
             path('Search/',csrf_exempt(search_Domain)),
             path('SearchP/',csrf_exempt(search_Plan)),
             path('XML/',csrf_exempt(distributor_data_for_xml)),]
