from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='Correo electrónico') # Hacemos el email único obligatorio

    # Esto le dice a Django que el campo para loguearse es el email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] # 'username' pasa a ser secundario

    def __str__(self):
        return self.email


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