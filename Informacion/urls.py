from Informacion import views
from django.urls import path



urlpatterns = [
    path('inicio/', views.inicio, name= 'inicio'),
    path('clientes/', views.clientes, name='clientes'),
    path('proveedores/', views.proveedores, name= 'proveedores'),
    path('compras/', views.compras, name='compras'),
    path('clientes-form/', views.clientes_form, name='ClientesForm'),
    path('proveedores-form/', views.proveedores_form, name='ProveedoresForm'),
    path('compras-form/', views.compras_form, name='ComprasForm'),
    path('busquedaClientes/', views.busquedaClientes, name='BusquedaClientes'),
    path('buscar/', views.buscar),
]

