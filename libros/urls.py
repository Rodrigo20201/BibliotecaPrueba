from django.urls import path
from . import views

urlpatterns = [
    path('listar/', views.listar_libros, name='listar_libros'),
    path('agregar/', views.agregar_libro, name='agregar_libro'),
    path('autor/agregar/', views.agregar_autor, name='agregar_autor'),
    path('categoria/agregar/', views.agregar_categoria, name='agregar_categoria'),
    path('tipo/agregar/', views.agregar_tipo, name='agregar_tipo')
]
