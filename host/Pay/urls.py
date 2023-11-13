from .views import Card_view,Pay_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('Card/', csrf_exempt(Card_view)),
             path('Pay/',csrf_exempt(Pay_view)),
             ]
