from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import RegistroProduccionForm
from .models import RegistroProduccion


def home(request):
    title = "Inicio"

    data = {
        "title" : title,
    }

    return render(request, 'proyecto_tlp/produccion.html',data)
@login_required
def registrar_produccion(request):
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') # Redirecciona a la vista home, se puede cambiar
    else:
        form = RegistroProduccionForm()
    return render(request, 'proyecto_tlp/registro_produccion.html', {'form': form})

@login_required
def modificar_produccion(request, pk):
    registro = get_object_or_404(RegistroProduccion, pk=pk, operador=request.user)
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST, instance=registro)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.modificado_por = request.user
            registro.fecha_modificacion = timezone.now()
            registro.save()
            return redirect('home')  # Redirecciona a la vista de home, recomendado cambiar
    else:
        form = RegistroProduccionForm(instance=registro)
    return render(request, 'proyecto_tlp/modificar_produccion.html', {'form': form})

@login_required
def listar_produccion(request):
    registros = RegistroProduccion.objects.filter(operador=request.user)
    return render(request, 'proyecto_tlp/listar_produccion.html', {'registros': registros})




