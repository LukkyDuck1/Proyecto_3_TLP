from django.contrib import admin
from .models import Producto, Planta, RegistroProduccion

admin.site.register(Producto)
admin.site.register(Planta)
admin.site.register(RegistroProduccion)
