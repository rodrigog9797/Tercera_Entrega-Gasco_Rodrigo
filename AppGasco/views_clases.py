from django.shortcuts import render
from AppGasco.models import Categoria, Producto, Cliente
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from .forms import UserRegisterForm
#from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
#from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class CategoriaListView(ListView):
    """
    Vista para mostrar una lista de todas las categorias.
    """
    model = Categoria  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_list.html"  # Plantilla para renderizar la lista

class CategoriaDetalle(DetailView):
    """
    Vista para mostrar los detalles de una categoria específica.
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_detalle.html"

class CategoriaCreateView(CreateView):
    """
    Vista para crear nuevas categorias a través de un formulario.
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_form.html"
    success_url = reverse_lazy("List_Categoria")  # URL de redirección después de crear un curso
    fields = ["nombre_categoria", "descripcion_categoria"]  # Campos del modelo a mostrar en el formulario

class CategoriaUpdateView(UpdateView):
    """
    Vista para editar categorias existentes a través de un formulario
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_edit.html"
    success_url = reverse_lazy("List_Categoria")
    fields = ["nombre_categoria", "descripcion_categoria"]

class CategoriaDeleteView(DeleteView):
    """
    Vista para eliminar categoria.
    """
    model = Categoria
    success_url = reverse_lazy("List_Categoria")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_confirm_delete.html"  # Plantilla para confirmar la eliminación

class ProductoListView(ListView):
    """
    Vista para mostrar una lista de todos los productos.
    """
    model = Producto  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Producto/producto_list.html"  # Plantilla para renderizar la lista

class ProductoDetalle(DetailView):
    """
    Vista para mostrar los detalles de un producto específico.
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_detalle.html"

class ProductoCreateView(CreateView):
    """
    Vista para crear nuevos productos a través de un formulario.
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_form.html"
    success_url = reverse_lazy("List_Producto")  # URL de redirección después de crear un curso
    fields = ["nombre_producto", "descripcion_producto", "precio", "stock", "categorias"]  # Campos del modelo a mostrar en el formulario

class ProductoUpdateView(UpdateView):
    """
    Vista para editar productos existentes a través de un formulario
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_edit.html"
    success_url = reverse_lazy("List_Producto")
    fields = ["nombre_producto", "descripcion_producto", "precio", "stock", "categorias"]

class ProductoDeleteView(DeleteView):
    """
    Vista para eliminar productos.
    """
    model = Producto
    success_url = reverse_lazy("List_Producto")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Producto/producto_confirm_delete.html"  # Plantilla para confirmar la eliminación

class ClienteListView(ListView):
    """
    Vista para mostrar una lista de todos los clientes.
    """
    model = Cliente  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_list.html"  # Plantilla para renderizar la lista

class ClienteDetalle(DetailView):
    """
    Vista para mostrar los detalles de un cliente específico.
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_detalle.html"

class ClienteCreateView(CreateView):
    """
    Vista para crear nuevos clientes a través de un formulario.
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_form.html"
    success_url = reverse_lazy("List_Cliente")  # URL de redirección después de crear un curso
    fields = ["nombre_cliente", "apellido", "email", "telefono", "direccion"]  # Campos del modelo a mostrar en el formulario

class ClienteUpdateView(UpdateView):
    """
    Vista para editar clientes existentes a través de un formulario
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_edit.html"
    success_url = reverse_lazy("List_Cliente")
    fields = ["nombre_cliente", "apellido", "email", "telefono", "direccion"]

class ClienteDeleteView(DeleteView):
    """
    Vista para eliminar cliente.
    """
    model = Cliente
    success_url = reverse_lazy("List_Cliente")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_confirm_delete.html"  # Plantilla para confirmar la eliminación