from django.contrib import admin
from django.urls import path, include
from proyecto_tlp import views

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', views.home, name="home"),
=======
    path('home/',views.home, name="home"),
>>>>>>> 316c78d3f7d1b147afdbb23bb649a963cfc363cc
    path('api/', include('rest.urls')),
    path('registrar/', views.registrar_produccion, name='registrar_produccion'),
    path('modificar/<int:pk>/', views.modificar_produccion, name='modificar_produccion'),
    path('listar/', views.listar_produccion, name='listar_produccion'),  # Agregar esta línea
]
