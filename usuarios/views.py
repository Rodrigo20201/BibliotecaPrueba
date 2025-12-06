from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroForm
from .models import PerfilUsuario
from django.contrib.auth.decorators import login_required

@login_required
def inicio_lector(request):
    return render(request, 'usuarios/inicio_lector.html')

@login_required
def dashboard_bibliotecario(request):
    return render(request, 'usuarios/dashboard_bibliotecario.html')

@login_required
def dashboard_admin(request):
    return render(request, 'usuarios/dashboard_admin.html')


def login_usuario(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            perfil = PerfilUsuario.objects.get(user=user)
            if perfil.rol.nombre_rol == "Lector":
                return redirect('inicio_lector')
            elif perfil.rol.nombre_rol == "Bibliotecario":
                return redirect('dashboard_bibliotecario')
            elif perfil.rol.nombre_rol == "Administrador":
                return redirect('dashboard_admin')
        else:
            return render(request, 'usuarios/login.html', {'error': 'Usuario o contraseña incorrectos'})
    return render(request, 'usuarios/login.html')

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('login')
