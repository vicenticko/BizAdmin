from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        # Aquí definimos qué campos queremos pedir en el registro
        # La contraseña y confirmación de contraseña ya vienen incluidas por UserCreationForm
        fields = ['username', 'first_name', 'last_name', 'email']