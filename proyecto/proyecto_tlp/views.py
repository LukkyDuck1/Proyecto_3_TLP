from django.shortcuts import render
from django.http import HttpResponse
import requests 
# Create your views here.
def home(request):
    title = "Inicio"

    data = {
        "title" : title,
    }

    return render(request, 'proyecto_tlp/produccion.html',data)
