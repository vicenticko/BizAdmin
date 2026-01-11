from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

def base(request):
    return render(request, 'core/base.html')

def login(request):
    return render(request, 'core/registration/login.html')

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Opcional: Si quieres que se loguee automáticamente al registrarse, descomenta la siguiente línea:
            # login(request, user)
            return redirect('login') # Redirige al login tras registrarse
    else:
        form = RegistroForm()
    
    return render(request, 'core/registration/register.html', {'form': form})