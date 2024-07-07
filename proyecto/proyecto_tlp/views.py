from django.shortcuts import render, redirect, get_object_or_404
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

def modificar_produccion(request, pk):
    registro = get_object_or_404(RegistroProduccion, pk=pk)
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('home') # Redirecciona a la vista home, se puede cambiar por la vista de listar produccion?
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'proyecto_tlp/modificar_produccion.html', {'form': form})



