from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class TipoLibro(models.Model):
    nombre_tipo = models.CharField(max_length=30)  # Físico/Digital/Audiolibro
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre_tipo

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    tipo = models.ForeignKey(TipoLibro, on_delete=models.SET_NULL, null=True)
    anio_publicacion = models.IntegerField()
    estado = models.CharField(max_length=50)  # Disponible, Prestado, etc.
    ejemplares_disponibles = models.IntegerField(default=1)
    url_digital = models.URLField(blank=True, null=True)
    imagen = models.ImageField(upload_to='portadas/', blank=True, null=True)  # imagen de portada

    def __str__(self):
        return self.titulo
