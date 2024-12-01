from django.shortcuts import render
from AppGasco.models import Categoria , Cliente , Producto
from django.http import HttpResponse
from AppGasco.forms import CategoriaFormulario , ClienteFormulario , ProductoFormulario
# Create your views here.

def inicio(request):
    return render(request, "appgasco/index.html")

def categoria(request):
    return render(request, "appgasco/categoria.html")

def producto(request):
    return render(request, "appgasco/producto.html")

def cliente(request):
    return render(request, "appgasco/cliente.html")

def categoriaFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = CategoriaFormulario(request.POST)  # Creamos un objeto formulario con los datos enviados

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            categoria = Categoria(nombre_categoria=informacion["nombre_categoria"], descripcion_categoria=informacion["descripcion_categoria"])  # Creamos un objeto Categoria
            categoria.save()  # Guardamos la categoria en la base de datos
            return render(request, "AppGasco/index.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = CategoriaFormulario()  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(request, "AppGasco/categoriaFormulario.html", {"miFormulario": miFormulario})

def busqueda_DescripcionCategoria(request):
    return render(request, "AppGasco/busqueda_DescripcionCategoria.html")

def buscar_categoria(request):
    if request.GET["descripcion_categoria"]:
        #me va a dar la respuesta del nombre de la categoria que estoy buscando
        descripcion_categoria = request.GET["descripcion_categoria"]
        categoria = Categoria.objects.filter(descripcion_categoria__icontains=descripcion_categoria)
        return render(request, "AppGasco/resultadosBusqueda.html", {"categoria": categoria, "descripcion_categoria": descripcion_categoria})

    else:

        respuesta = "No enviaste ningún dato"
    
    return HttpResponse(respuesta)


def clienteFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = ClienteFormulario(request.POST)  # Creamos un objeto formulario con los datos enviados

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            cliente = Cliente(nombre_cliente=informacion["nombre_cliente"], apellido=informacion["apellido"],email=informacion["email"], telefono=informacion["telefono"], direccion=informacion["direccion"])  # Creamos un objeto Cliente
            cliente.save()  # Guardamos el cliente en la base de datos
            return render(request, "AppGasco/index.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = ClienteFormulario()  # Creamos un formulario vacío para mostrarlo inicialmente

    return render(request, "AppGasco/clienteFormulario.html", {"miFormulario": miFormulario})

def busqueda_NombreCliente(request):
    return render(request, "AppGasco/busqueda_NombreCliente.html")

def buscar_cliente(request):

    if request.GET["nombre_cliente"]:
        nombre_cliente = request.GET["nombre_cliente"]
        cliente = Cliente.objects.filter(nombre_cliente__icontains=nombre_cliente)
        return render(request, "AppGasco/resultadosBusqueda.html", {"cliente": cliente, "nombre_cliente": nombre_cliente})

    else:

        respuesta = "No enviaste ningún dato"
    
    return HttpResponse(respuesta)

def productoFormulario(request):
    if request.method == "POST":  # Si el formulario fue enviado
        miFormulario = ProductoFormulario(request.POST)  # Creamos un objeto formulario con los datos enviados

        if miFormulario.is_valid():  # Verificamos si los datos son válidos
            informacion = miFormulario.cleaned_data  # Obtenemos los datos limpios y validados
            producto = Producto(nombre_producto=informacion["nombre_producto"], descripcion_producto=informacion["descripcion_producto"],precio=informacion["precio"], stock=informacion["stock"], categorias=informacion["categorias"])  # Creamos un objeto Producto
            producto.save()  # Guardamos el producto en la base de datos
            return render(request, "AppGasco/index.html")  # Redirigimos a la página de inicio
    else:
        miFormulario = ProductoFormulario()  # Creamos un formulario vacío para mostrarlo inicialmente
    
    return render(request, "AppGasco/productoFormulario.html", {"miFormulario": miFormulario})

def busqueda_NombreProducto(request):
    return render(request, "AppGasco/busqueda_NombreProducto.html")

def buscar_producto(request):

    if request.GET["nombre_producto"]:
        nombre_producto = request.GET["nombre_producto"]
        productos = Producto.objects.filter(nombre_producto__icontains=nombre_producto)
        return render(request, "AppGasco/resultadosBusqueda.html", {"productos": productos, "nombre_producto": nombre_producto})

    else:

        respuesta = "No enviaste ningún dato"
    
    return HttpResponse(respuesta)

