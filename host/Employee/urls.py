from .views import Employee_view,Ticket_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('Employees/', csrf_exempt(Employee_view)),
             path('Ticket/',csrf_exempt(Ticket_view)),
             ]
