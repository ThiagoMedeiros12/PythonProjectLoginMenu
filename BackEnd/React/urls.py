from django.urls import path
from .import views

urlpatterns = [
	path('',views.IndexView),
	path('Sucess',views.loginIndex),
	]