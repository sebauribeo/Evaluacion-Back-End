from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def vista1(request):
    return render(request, 'vista1.html')

def vista2(request):
    return render(request, 'vista2.html')

def vista3(request):
    return render(request, 'vista3.html')

def vista4(request):
    return render(request, 'vista4.html')

def vista5(request):
    return render(request, 'vista5.html')