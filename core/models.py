from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # Aquí puedes añadir campos personalizados para tu negocio
    email = models.EmailField(unique=True, verbose_name='Correo electrónico')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    creado_el = models.DateTimeField(auto_now_add=True)
    
    # Esto vincula el cliente al usuario que lo registró (opcional)
    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nombre