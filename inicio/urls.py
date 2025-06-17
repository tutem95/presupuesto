from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página principal una vez logueado
    path('registro/', views.registro, name='registro'),  # Registro de usuario
]
