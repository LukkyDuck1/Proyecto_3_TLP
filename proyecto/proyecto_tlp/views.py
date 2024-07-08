from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils import timezone
from .forms import RegistroProduccionForm
from .models import RegistroProduccion, Producto
from .slack import enviar_slack
import requests

#Se define el home
def home(request):
    title = "Inicio"
    data = {
        "title": title,
    }
    return render(request, 'proyecto_tlp/home.html', data)

def exit(request):
    logout(request)
    return redirect('home')

#Se define funcion para registrar 
@login_required
def registrar_produccion(request):
    
    if request.method == 'POST':
        form = RegistroProduccionForm(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.operador = request.user
            
            registro.save()
            #Por desconocimiento en autenticacion para api (consideramos que no era solucion un AllowAny ya que perdia la caracteristica de que solo un usuario autenticado podria usar la api)
            mensaje=str(registro.fecha_produccion)+" | " +str(registro.hora_registro)+" | " +str(registro.planta)+"- Nuevo registro de produccion -"+str(registro.producto)+" | " +str(registro.cantidad) +"|Total almacenado:"+str(requests.get('http://127.0.0.1:8000/api/registro-produccion/'))
            #Se envia mensaje via slack
            enviar_slack(mensaje)
            return redirect('home')
    else:
        form = RegistroProduccionForm()
    productos = Producto.objects.all()
    print(productos)  # Verificar los productos en la consola del servidor
    return render(request, 'proyecto_tlp/produccion.html', {'form': form, 'productos': productos})

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

#Funcion listar produccion
def listar_produccion(request):
    #aplica el filtro segun que el operador sea el user rquest
    registros = RegistroProduccion.objects.filter(operador=request.user)
    return render(request, 'proyecto_tlp/listar_produccion.html', {'registros': registros})




