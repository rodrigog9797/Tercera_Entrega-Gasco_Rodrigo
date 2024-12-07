from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from Users.forms import UserRegisterForm

# Create your views here.


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
                return render(request, "Users/login.html", {"mensaje":"Error, datos incorrectos", "form": form})  # Renderiza el formulario de login con un mensaje de error
        else:  # Si el formulario no es válido
            return render(request, "AppGasco/index.html", {"mensaje":"Error, formulario inválido"})  # Renderiza la plantilla con un mensaje de error

    form = AuthenticationForm()  # Si es una solicitud GET (primera vez que se accede a la página), crea un formulario vacío
    return render(request, "Users/login.html", {"form":form})  # Renderiza el formulario de login


# Vista de registro
def register(request):

    if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request,"AppGasco/index.html" ,  {"mensaje":"Usuario Creado :)"})

    else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

    return render(request,"Users/registro.html" ,  {"form":form})