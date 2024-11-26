from django import forms

class CategoriaFormulario(forms.Form):
    nombre_categoria = forms.CharField(max_length=30)
    descripcion_categoria = forms.CharField()

class Buscar(forms.Form):
    nombre = forms.CharField(max_length=30)

class ClienteFormulario(forms.Form):
    nombre_cliente = forms.CharField(max_length=30)
    apellido = forms.CharField()
    email = forms.EmailField()
    telefono = forms.CharField()
    direccion = forms.CharField()

class ProductoFormulario(forms.Form):
    nombre_producto = forms.CharField(max_length=30)
    descripcion_producto = forms.CharField(max_length=500)
    precio = forms.DecimalField(max_digits=10, decimal_places=2)
    stock = forms.IntegerField()
    categorias = forms.CharField(max_length=30)