from django.shortcuts import render
from AppGasco.models import Categoria, Producto, Cliente
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

class AdminOUsuarioComunMixin:
    """
    Mixin que permite el acceso a usuarios que pertenecen a los grupos
    'Administrador' o 'Usuarios comunes'.
    Esto lo hago para no repetir lo mismo en todas las clases, y simplemente deba agregar el argumento en aquellas clases que lo necesite
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name__in=['Administrador', 'Usuarios comunes']).exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        
class AdminRequiredMixin:
    """
    Mixin que permite el acceso solo a usuarios que pertenecen al grupo 'Administrador'.
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.groups.filter(name='Administrador').exists():
            return super().dispatch(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("No tienes permiso para acceder a esta página, solo el Administrador del sitio puede hacerlo.")



class CategoriaListView(ListView):
    """
    Vista para mostrar una lista de todas las categorias.
    """
    model = Categoria  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_list.html"  # Plantilla para renderizar la lista

class CategoriaDetalle(LoginRequiredMixin,AdminOUsuarioComunMixin,DetailView):
    """
    Vista para mostrar los detalles de una categoria específica.
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_detalle.html"
    login_url = reverse_lazy('Login')

class CategoriaCreateView(LoginRequiredMixin,AdminOUsuarioComunMixin,CreateView):
    """
    Vista para crear nuevas categorias a través de un formulario.
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_form.html"
    success_url = reverse_lazy("List_Categoria")  # URL de redirección después de crear un curso
    fields = ["nombre_categoria", "descripcion_categoria"]  # Campos del modelo a mostrar en el formulario
    login_url = reverse_lazy('Login')

class CategoriaUpdateView(LoginRequiredMixin,AdminOUsuarioComunMixin,UpdateView):
    """
    Vista para editar categorias existentes a través de un formulario
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_edit.html"
    success_url = reverse_lazy("List_Categoria")
    fields = ["nombre_categoria", "descripcion_categoria"]
    login_url = reverse_lazy('Login')

class CategoriaDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
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

class ProductoDetalle(LoginRequiredMixin,AdminOUsuarioComunMixin,DetailView):
    """
    Vista para mostrar los detalles de un producto específico.
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_detalle.html"
    login_url = reverse_lazy('Login')

class ProductoCreateView(LoginRequiredMixin,AdminOUsuarioComunMixin,CreateView):
    """
    Vista para crear nuevos productos a través de un formulario.
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_form.html"
    success_url = reverse_lazy("List_Producto")  # URL de redirección después de crear un curso
    fields = ["nombre_producto", "descripcion_producto", "precio", "stock", "categorias"]  # Campos del modelo a mostrar en el formulario
    login_url = reverse_lazy('Login')

class ProductoUpdateView(LoginRequiredMixin,AdminOUsuarioComunMixin,UpdateView):
    """
    Vista para editar productos existentes a través de un formulario
    """
    model = Producto
    template_name = "appgasco/Vistas_Clase_Producto/producto_edit.html"
    success_url = reverse_lazy("List_Producto")
    fields = ["nombre_producto", "descripcion_producto", "precio", "stock", "categorias"]
    login_url = reverse_lazy('Login')

class ProductoDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
    """
    Vista para eliminar productos.
    """
    model = Producto
    success_url = reverse_lazy("List_Producto")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Producto/producto_confirm_delete.html"  # Plantilla para confirmar la eliminación
    login_url = reverse_lazy('Login')

class ClienteListView(LoginRequiredMixin,AdminRequiredMixin,ListView):
    """
    Vista para mostrar una lista de todos los clientes.
    """
    model = Cliente  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_list.html"  # Plantilla para renderizar la lista
    login_url = reverse_lazy('Login')

class ClienteDetalle(LoginRequiredMixin,AdminRequiredMixin,DetailView):
    """
    Vista para mostrar los detalles de un cliente específico.
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_detalle.html"
    login_url = reverse_lazy('Login')

class ClienteCreateView(LoginRequiredMixin,AdminRequiredMixin,CreateView):
    """
    Vista para crear nuevos clientes a través de un formulario.
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_form.html"
    success_url = reverse_lazy("List_Cliente")  # URL de redirección después de crear un curso
    fields = ["nombre_cliente", "apellido", "email", "telefono", "direccion"]  # Campos del modelo a mostrar en el formulario
    login_url = reverse_lazy('Login')

class ClienteUpdateView(LoginRequiredMixin,AdminRequiredMixin,UpdateView):
    """
    Vista para editar clientes existentes a través de un formulario
    """
    model = Cliente
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_edit.html"
    success_url = reverse_lazy("List_Cliente")
    fields = ["nombre_cliente", "apellido", "email", "telefono", "direccion"]
    login_url = reverse_lazy('Login')

class ClienteDeleteView(LoginRequiredMixin,AdminRequiredMixin,DeleteView):
    """
    Vista para eliminar cliente.
    """
    model = Cliente
    success_url = reverse_lazy("List_Cliente")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Cliente/cliente_confirm_delete.html"  # Plantilla para confirmar la eliminación
    login_url = reverse_lazy('Login')