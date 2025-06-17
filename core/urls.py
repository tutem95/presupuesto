from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', include('inicio.urls')),  # Rutas de la app de autenticación
    path('login/', auth_views.LoginView.as_view(template_name='inicio/login.html'), name='login'),
    path('inicio/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
