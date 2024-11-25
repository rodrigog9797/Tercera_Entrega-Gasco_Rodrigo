from django.shortcuts import render
from AppGasco.models import Categoria
from django.http import HttpResponse
from AppGasco.forms import CategoriaFormulario
# Create your views here.

def inicio(request):
    return render(request, "appgasco/padre.html")

def categoria(request):
    return render(request, "appgasco/categoria.html")

def producto(request):
    return render(request, "appgasco/producto.html")

def cliente(request):
    return render(request, "appgasco/cliente.html")

def categoriaFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = CategoriaFormulario(request.POST)  # Creamos un objeto formulario con los datos enviados
        print(miFormulario)  # Imprimimos el formulario para depuración (opcional)

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            categoria = Categoria(nombre_categoria=informacion["nombre_categoria"], descripcion_categoria=informacion["descripcion_categoria"])  # Creamos un objeto Categoria
            categoria.save()  # Guardamos la categoria en la base de datos
            return render(request, "AppGasco/index.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = CategoriaFormulario()  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(request, "AppGasco/categoriaFormulario.html", {"miFormulario": miFormulario})





# def categoria(self):
#     categoria = Categoria(nombre = "Celulares", descripcion = "Celulares disponibles")
#     categoria.save()

#     vista = f"Categoria : {categoria.nombre}  Descripción: {categoria.descripcion}"

#     return HttpResponse(vista)