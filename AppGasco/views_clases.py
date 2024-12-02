from django.shortcuts import render
from AppGasco.models import Categoria, Producto, Cliente
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

def login_request(request):
    """
    Función para manejar las solicitudes de inicio de sesión.
    """
    if request.method == "POST":  # Si el formulario fue enviado (método POST)
        form = AuthenticationForm(request, data=request.POST)  # Crea un formulario y lo llena con los datos enviados
        print(form)  # Imprime el formulario en la consola (para depuración)

        if form.is_valid():  # Si el formulario es válido
            usuario = form.cleaned_data.get("username")  # Obtiene el nombre de usuario
            clave = form.cleaned_data.get("password")  # Obtiene la contraseña

            nombre_usuario = authenticate(username=usuario, password=clave)  # Intenta autenticar al usuario

            if nombre_usuario is not None:  # Si la autenticación es exitosa
                login(request, nombre_usuario)  # Inicia la sesión del usuario
                return render(request, "AppGasco/index.html", {"mensaje":f"Has iniciado sesión. Bienvenido {usuario}"})  # Renderiza la plantilla con un mensaje de bienvenida
            else:  # Si la autenticación falla
                form = AuthenticationForm()  # Crea un nuevo formulario vacío
                return render(request, "AppGasco/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  # Renderiza el formulario de login con un mensaje de error
        else:  # Si el formulario no es válido
            return render(request, "AppGasco/index.html", {"mensaje":"Error, formulario inválido"})  # Renderiza la plantilla con un mensaje de error

    form = AuthenticationForm()  # Si es una solicitud GET (primera vez que se accede a la página), crea un formulario vacío
    return render(request, "AppGasco/login.html", {"form":form})  # Renderiza el formulario de login



class CategoriaListView(ListView):
    """
    Vista para mostrar una lista de todas las categorias.
    """
    model = Categoria  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_list.html"  # Plantilla para renderizar la lista

class CategoriaDetalle(LoginRequiredMixin,DetailView):
    """
    Vista para mostrar los detalles de una categoria específica.
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_detalle.html"
    login_url = reverse_lazy('Login')

class CategoriaCreateView(LoginRequiredMixin,CreateView):
    """
    Vista para crear nuevas categorias a través de un formulario.
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_form.html"
    success_url = reverse_lazy("List_Categoria")  # URL de redirección después de crear un curso
    fields = ["nombre_categoria", "descripcion_categoria"]  # Campos del modelo a mostrar en el formulario
    login_url = reverse_lazy('Login')

class CategoriaUpdateView(LoginRequiredMixin,UpdateView):
    """
    Vista para editar categorias existentes a través de un formulario
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_edit.html"
    success_url = reverse_lazy("List_Categoria")
    fields = ["nombre_categoria", "descripcion_categoria"]
    login_url = reverse_lazy('Login')

class CategoriaDeleteView(LoginRequiredMixin,DeleteView):
    """
    Vista para eliminar categoria.
    """
    model = Categoria
    success_url = reverse_lazy("List_Categoria")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_confirm_delete.html"  # Plantilla para confirmar la eliminación
    login_url = reverse_lazy('Login')

class ProductoListView(ListView):
    """
    Vista para mostrar una lista de todos los productos.
    """
    model = Producto  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Producto/producto_list.html"  # Plantilla para renderizar la lista

class ProductoDetalle(LoginRequiredMixin,DetailView):
    """
    Vista para mostrar los detalles de un producto específico.
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_detalle.html"
    login_url = reverse_lazy('Login')

class ProductoCreateView(LoginRequiredMixin,CreateView):
    """
    Vista para crear nuevos productos a través de un formulario.
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_form.html"
    success_url = reverse_lazy("List_Producto")  # URL de redirección después de crear un curso
    fields = ["nombre_producto", "descripcion_producto", "precio", "stock", "categorias"]  # Campos del modelo a mostrar en el formulario
    login_url = reverse_lazy('Login')

class ProductoUpdateView(LoginRequiredMixin,UpdateView):
    """
    Vista para editar productos existentes a través de un formulario
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_edit.html"
    success_url = reverse_lazy("List_Producto")
    fields = ["nombre_producto", "descripcion_producto", "precio", "stock", "categorias"]
    login_url = reverse_lazy('Login')

class ProductoDeleteView(LoginRequiredMixin,DeleteView):
    """
    Vista para eliminar productos.
    """
    model = Producto
    success_url = reverse_lazy("List_Producto")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Producto/producto_confirm_delete.html"  # Plantilla para confirmar la eliminación
    login_url = reverse_lazy('Login')

class ClienteListView(LoginRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los clientes.
    """
    model = Cliente  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_list.html"  # Plantilla para renderizar la lista
    login_url = reverse_lazy('Login')

class ClienteDetalle(LoginRequiredMixin,DetailView):
    """
    Vista para mostrar los detalles de un cliente específico.
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_detalle.html"
    login_url = reverse_lazy('Login')

class ClienteCreateView(LoginRequiredMixin,CreateView):
    """
    Vista para crear nuevos clientes a través de un formulario.
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_form.html"
    success_url = reverse_lazy("List_Cliente")  # URL de redirección después de crear un curso
    fields = ["nombre_cliente", "apellido", "email", "telefono", "direccion"]  # Campos del modelo a mostrar en el formulario
    login_url = reverse_lazy('Login')

class ClienteUpdateView(LoginRequiredMixin,UpdateView):
    """
    Vista para editar clientes existentes a través de un formulario
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_edit.html"
    success_url = reverse_lazy("List_Cliente")
    fields = ["nombre_cliente", "apellido", "email", "telefono", "direccion"]
    login_url = reverse_lazy('Login')

class ClienteDeleteView(LoginRequiredMixin,DeleteView):
    """
    Vista para eliminar cliente.
    """
    model = Cliente
    success_url = reverse_lazy("List_Cliente")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_confirm_delete.html"  # Plantilla para confirmar la eliminación
    login_url = reverse_lazy('Login')