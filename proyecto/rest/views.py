from rest_framework import viewsets
from rest_framework import permissions
from proyecto_tlp.models import RegistroProduccion, Producto, Planta
from .serializers import RegistroSerializer, ProductoSerializer, PlantaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated




class RegistroProduccionViewSet(viewsets.ModelViewSet):

    queryset = RegistroProduccion.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [permissions.IsAuthenticated]

    # http://127.0.0.1:8000/api/registro-produccion/?year=2024&month=7
    #Aplicar filtro de año y mes para solicitud
    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.query_params.get('year')
        month = self.request.query_params.get('month')
        
        if year is not None:
            queryset = queryset.filter(fecha_produccion__year=year)
        if month is not None:
            queryset = queryset.filter(fecha_produccion__month=month)
        
        return queryset    

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticated]

class PlantaViewSet(viewsets.ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer
    permission_classes = [permissions.IsAuthenticated]

#Devuelve la sum de los registros
class ProduccionTotalListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        registros = RegistroProduccion.objects.all()
        total_produccion = sum(registro.cantidad for registro in registros)
        return Response({'total_produccion': total_produccion})    