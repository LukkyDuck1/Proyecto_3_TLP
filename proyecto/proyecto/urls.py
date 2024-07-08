from django.contrib import admin
from django.urls import path, include
from proyecto_tlp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name="home"),

    path('api/', include('rest.urls')),

    path('registrar/', views.registrar_produccion, name='registrar_produccion'),

    path('modificar/<int:pk>/', views.modificar_produccion, name='modificar_produccion'),

    path('listar/', views.listar_produccion, name='listar_produccion'), 

    path('',include('django.contrib.auth.urls')),
    
    path('home/', views.exit, name='exit'),
]
