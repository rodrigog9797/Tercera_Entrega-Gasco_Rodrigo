from django.contrib import admin
from django.urls import path, include
from AppGasco import views

urlpatterns = [
    path('inicio/', views.inicio, name = "inicio"),
    path('categoria/', views.categoria, name = "categoria"),
    path('producto/', views.producto, name = "producto"),
    path('cliente/', views.cliente, name = "cliente"),
    path('categoriaFormulario/', views.categoriaFormulario, name = "CategoriaFormulario"),
    path('busqueda_DescripcionCategoria/', views.busqueda_DescripcionCategoria, name = "Busqueda_DescripcionCategoria"),
    path('AppGasco/buscar_categoria/', views.buscar_categoria, name="buscar_categoria"),
    path('clienteFormulario/', views.clienteFormulario, name = "ClienteFormulario"),
    path('busqueda_NombreCliente/', views.busqueda_NombreCliente, name = "Busqueda_NombreCliente"),
    path('AppGasco/buscar_cliente/', views.buscar_cliente, name="buscar_cliente"),
    path('productoFormulario/', views.productoFormulario, name = "ProductoFormulario"),
    path('busqueda_NombreProducto/', views.busqueda_NombreProducto, name = "Busqueda_NombreProducto"),
    path('AppGasco/buscar_producto/', views.buscar_producto, name="buscar_producto"),

    












]   