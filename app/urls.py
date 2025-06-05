
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.vistaAModificar, name='hola'),
]