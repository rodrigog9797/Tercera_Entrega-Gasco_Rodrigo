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
    Vista para mostrar una lista de todos los cursos.
    """
    model = Categoria  # Modelo con el que trabaja esta vista
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_list.html"  # Plantilla para renderizar la lista

class CategoriaDetalle(DetailView):
    """
    Vista para mostrar los detalles de un curso específico.
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_detalle.html"

class CategoriaCreateView(CreateView):
    """
    Vista para crear nuevos cursos a través de un formulario.
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_form.html"
    success_url = reverse_lazy("List")  # URL de redirección después de crear un curso
    fields = ["nombre_categoria", "descripcion_categoria"]  # Campos del modelo a mostrar en el formulario

class CategoriaUpdateView(UpdateView):
    """
    Vista para editar cursos existentes a través de un formulario
    """
    model = Categoria
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_edit.html"
    success_url = reverse_lazy("List")
    #success_url = "/clases/lista/"  # Otra forma de especificar la URL de redirección
    fields = ["nombre_categoria", "descripcion_categoria"]

class CategoriaDeleteView(DeleteView):
    """
    Vista para eliminar cursos.
    """
    model = Categoria
    success_url = reverse_lazy("List")  # URL de redirección después de eliminar un curso
    template_name = "appgasco/Vistas_Clase_Categoria/categoria_confirm_delete.html"  # Plantilla para confirmar la eliminación

