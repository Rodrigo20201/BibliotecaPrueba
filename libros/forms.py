from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'categoria', 'tipo', 'anio_publicacion', 'estado', 'ejemplares_disponibles', 'url_digital', 'imagen']
