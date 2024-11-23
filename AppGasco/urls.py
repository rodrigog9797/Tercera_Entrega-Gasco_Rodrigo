from django.contrib import admin
from django.urls import path, include
from AppGasco import views

urlpatterns = [
    #path('', include('AppGasco.urls')),
    path('inicio/', views.inicio),
    path('categoria/', views.categoria),
    path('producto/', views.producto),
    path('cliente/', views.cliente),
]