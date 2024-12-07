from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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

# class UserRegisterForm(UserCreationForm):
#     email = forms.EmailField()
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ["username", "email", "password1", "password2"]
#         # Si queremos EDIAR los mensajes de ayuda editamos este dict,
#             # de lo contrario lo limpiamos de ésta forma.
#         help_text = {k: "" for k in fields}