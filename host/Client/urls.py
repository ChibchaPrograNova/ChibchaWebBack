from .views import user_view,Plan_view,Plan_Client_view
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[path('Manage/', csrf_exempt(user_view)),
             path('Plan/',csrf_exempt(Plan_view)),
             path('Plan-Client/',csrf_exempt(Plan_Client_view))
             ]
