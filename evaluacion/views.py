from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def productos(request):
    return render(request, 'productos.html')  

def contacto(request):
    return render(request, 'contacto.html')

def inventario(request):
    return render(request, 'inventario.html')

def admin(request):
    return render(request, 'admin.html')

