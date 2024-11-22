from django.shortcuts import render
from AppGasco.models import Categoria
from django.http import HttpResponse
# Create your views here.

def categoria(self):
    categoria = Categoria(nombre = "Celulares", descripcion = "Celulares disponibles")
    categoria.save()

    vista = f"Categoria : {categoria.nombre}  Descripción: {categoria.descripcion}"

    return HttpResponse(vista)