from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("reactpy/", include("reactpy_django.http.urls")),
    path('', include('React.urls')),
    
]
