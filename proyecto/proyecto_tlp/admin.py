from django.contrib import admin
from .models import Producto, Planta, RegistroProduccion
from django.utils import timezone

class RegistroProduccionAdmin(admin.ModelAdmin):
    list_display = ('producto', 'planta', 'cantidad', 'fecha_produccion', 'turno', 'hora_registro', 'operador', 'anulado', 'anulado_por', 'fecha_anulacion')
    actions = ['anular_registros']

    def anular_registros(self, request, queryset):
        for registro in queryset:
            registro.anulado = True
            registro.anulado_por = request.user
            registro.fecha_anulacion = timezone.now()
            registro.save()

    anular_registros.short_description = "Anular registros seleccionados"

admin.site.register(Producto)
admin.site.register(Planta)
admin.site.register(RegistroProduccion, RegistroProduccionAdmin)
