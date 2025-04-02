from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='mainMenu'),
    path('logon', views.logon, name='loginLogon'),
]