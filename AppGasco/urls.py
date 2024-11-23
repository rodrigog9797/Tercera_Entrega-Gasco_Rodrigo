from django.contrib import admin
from django.urls import path, include
from AppGasco import views

urlpatterns = [
    #path('', include('AppGasco.urls')),
    path('inicio/', views.inicio, name = "inicio"),
    path('categoria/', views.categoria, name = "categoria"),
    path('producto/', views.producto, name = "producto"),
    path('cliente/', views.cliente, name = "cliente"),
]