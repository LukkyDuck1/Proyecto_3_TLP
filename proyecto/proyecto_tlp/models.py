from django.db import models
from django.contrib.auth.models import User

class Planta(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)

class Producto(models.Model):
    codigo = models.CharField(max_length=10, unique=True)
    nombre = models.CharField(max_length=100)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name='productos', null=True, blank=True)


class RegistroProduccion(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    fecha_produccion = models.DateField()
    turno = models.CharField(max_length= 2, choices=(('AM', 'Mañana'), ('PM', 'Tarde'), ('MM', 'Noche')))
    hora_registro = models.DateTimeField(auto_now_add=True)
    operador = models.ForeignKey(User, on_delete=models.CASCADE)
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='modificador', null=True, blank=True)
    fecha_modificacion = models.DateTimeField(null=True, blank=True)
    

    
