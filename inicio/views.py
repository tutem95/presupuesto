from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

@login_required
def inicio(request):
    return render(request, 'inicio/inicio.html')

def pagina_inicio(request):
    return render(request, 'inicio/pagina_inicio.html')
