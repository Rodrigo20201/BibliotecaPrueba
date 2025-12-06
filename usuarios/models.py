from django.contrib.auth.models import User
from django.db import models

class RolUsuario(models.Model):
    nombre_rol = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre_rol

class PerfilUsuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(RolUsuario, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
