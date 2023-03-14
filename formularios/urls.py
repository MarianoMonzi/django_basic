from django.urls import path
from . import views

urlpatterns = [    
    path('', views.index, name="index"),
    path('empleados/', views.empleados, name="empleados"),
    path('clientes/', views.clientes, name="clientes"),
    path('productos/', views.productos, name="productos"),
    path('crear_producto/', views.crear_producto, name="crear_producto"),
    path('crear_clientes/', views.crear_clientes, name="crear_clientes"),
    path('crear_empleado/', views.crear_empleado, name="crear_empleado")
]