from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def base(request):
    return render(request, 'core/base.html')

def login(request):
    return render(request, 'core/registration/login.html')