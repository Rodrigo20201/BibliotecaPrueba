from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Autor, Categoria, TipoLibro, Libro
from .forms import LibroForm

@login_required
def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

@login_required
def agregar_libro(request):
    # Solo bibliotecarios
    if not hasattr(request.user, 'perfilusuario') or request.user.perfilusuario.rol.nombre_rol != 'Bibliotecario':
        return redirect('inicio_lector')

    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_libros')
    else:
        form = LibroForm()

    return render(request, 'libros/agregar_libro.html', {'form': form})

@login_required
def agregar_autor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Autor.objects.create(nombre=nombre)
        return redirect('agregar_libro')
    return render(request, 'libros/agregar_autor.html')

@login_required
def agregar_categoria(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        Categoria.objects.create(nombre=nombre)
        return redirect('agregar_libro')
    return render(request, 'libros/agregar_categoria.html')

@login_required
def agregar_tipo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        TipoLibro.objects.create(nombre_tipo=nombre)
        return redirect('agregar_libro')
    return render(request, 'libros/agregar_tipo.html')
