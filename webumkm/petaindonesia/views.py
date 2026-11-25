from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, 'petaindonesia/landing.html')

def welcome(request):
    return HttpResponse("<h1>Selamat Datang di Situs Kami !</h1>")

# Create your views here.
