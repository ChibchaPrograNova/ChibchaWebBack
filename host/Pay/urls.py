from .views import Card_view,Pay_view,Payment_Method_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('Card/', csrf_exempt(Card_view)),
             path('Pay/',csrf_exempt(Pay_view)),
             path('Payment_Method/',csrf_exempt(Payment_Method_view))
             ]
