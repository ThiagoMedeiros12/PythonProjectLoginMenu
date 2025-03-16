from django.urls import path
from . import  views
from django.contrib import admin


urlpatterns = [
    path("login-screen",views.index,name="login"),
    path("main-menu/",)
    ]