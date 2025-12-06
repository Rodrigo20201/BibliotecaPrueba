from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PerfilUsuario, RolUsuario

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Obtener el rol por defecto
        rol_lector = RolUsuario.objects.get(nombre_rol='Lector')
        
        # Crear el perfil con ese rol
        PerfilUsuario.objects.create(user=instance, rol=rol_lector)
