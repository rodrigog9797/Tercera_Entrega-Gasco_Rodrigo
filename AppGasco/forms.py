from django import forms

class CategoriaFormulario(forms.Form):
    nombre_categoria = forms.CharField(max_length=30)
    descripcion_categoria = forms.CharField()