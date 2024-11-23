from django.shortcuts import render
from AppGasco.models import Categoria
from django.http import HttpResponse
# Create your views here.

def inicio(request):
    return render(request, "appgasco/padre.html")

def categoria(request):
    return render(request, "appgasco/categoria.html")

def producto(request):
    return render(request, "appgasco/producto.html")

def cliente(request):
    return render(request, "appgasco/cliente.html")






# def categoria(self):
#     categoria = Categoria(nombre = "Celulares", descripcion = "Celulares disponibles")
#     categoria.save()

#     vista = f"Categoria : {categoria.nombre}  Descripción: {categoria.descripcion}"

#     return HttpResponse(vista)