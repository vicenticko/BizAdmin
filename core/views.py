from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'core/home.html')

def base(request):
    return render(request, 'core/base.html')

def login(request):
    return render(request, 'core/registration/login.html')