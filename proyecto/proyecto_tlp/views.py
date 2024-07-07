from django.shortcuts import render, redirect
from .forms import RegistroProduccionForm
from .models import RegistroProduccion

def home(request):
    title = "Inicio"

    data = {
        "title" : title,
    }

    return render(request, 'proyecto_tlp/produccion.html',data)

def registrar_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # Redirecciona a la vista home, se puede cambiar
    else:
        form = RegistroProduccionForm()
    return render(request, 'proyecto_tlp/registro_produccion.html', {'form': form})

