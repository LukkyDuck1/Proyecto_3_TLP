
from rest_framework import serializers
from proyecto_tlp import models


class ProductoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Producto
        fields = ['codigo', 'nombre', 'planta']

class PlantaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Planta
        fields = ['codigo', 'nombre']

class RegistroSerializer(serializers.HyperlinkedModelSerializer):
    #Sacamos los valores de producto y planta, para poder presentarlos en la vision de la api general. 
    producto = serializers.HyperlinkedRelatedField(view_name='producto-detail', queryset=models.Producto.objects.all())
    planta = serializers.HyperlinkedRelatedField(view_name='planta-detail', queryset=models.Planta.objects.all())

    class Meta:
        model = models.RegistroProduccion
        fields = ['producto', 'planta', 'cantidad', 'fecha_produccion', 'turno']