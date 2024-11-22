from django.http import HttpResponse
from django.template import Template, Context, loader
from django.shortcuts import render
##### El <h1> ... <h1> me sirve para hacer un titulo

def saludo(request):
    return HttpResponse("<h1>Hola, esta es la primera prueba de la pagina web<h1>")

def segunda_vista(request):
    return HttpResponse("Segunda vista")