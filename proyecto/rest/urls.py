from django.urls import include, path
from rest_framework import routers
from .views import RegistroProduccionViewSet, ProductoViewSet, PlantaViewSet, ProduccionTotalListView


#Aplicamos los routers
router = routers.DefaultRouter()
router.register(r'registro-produccion', RegistroProduccionViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'plantas', PlantaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #Para mostrar la sum de la produccion http://127.0.0.1:8000/api/registro-produccion/
    path('produccion-total/', ProduccionTotalListView.as_view(), name='produccion-total'),
    
]