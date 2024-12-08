from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from Users.forms import UserRegisterForm, UserEditForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            clave = form.cleaned_data.get("password")
            nombre_usuario = authenticate(username=usuario, password=clave)
            if nombre_usuario is not None:
                login(request, nombre_usuario)
                next_url = request.GET.get('next', 'inicio')  # Asegúrate de usar una URL absoluta
                return redirect(next_url)
            else:
                form = AuthenticationForm()
                return render(request, "Users/login.html", {"mensaje": "Error, datos incorrectos", "form": form})
        else:
            return render(request, "Users/login.html", {"mensaje": "Formulario inválido", "form": form})

    form = AuthenticationForm()
    return render(request, "Users/login.html", {"form": form})


# Vista de registro
def register(request):

    if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                username = form.cleaned_data['username']
                form.save()
                return render(request,"Users/registro.html" ,  {"mensaje":"Usuario Creado con éxito"})

    else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

    return render(request,"Users/registro.html" ,  {"form":form})

@login_required
def editar_perfil(request):
    """
    Vista para que los usuarios editen su perfil y cambien su contraseña sin cerrar la sesión.
    """
    user = request.user
    mensaje_exito = None

    # Inicializar los formularios para que siempre estén disponibles
    form = UserEditForm(instance=user)
    password_form = PasswordChangeForm(user=user)

    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'profile_form':  # Procesar formulario de perfil
            form = UserEditForm(request.POST, instance=user)
            if form.is_valid():
                form.save()
                mensaje_exito = "¡Tu perfil ha sido actualizado exitosamente!"

        elif form_type == 'password_form':  # Procesar formulario de contraseña
            password_form = PasswordChangeForm(user=user, data=request.POST)
            if password_form.is_valid():
                password_form.save()
                update_session_auth_hash(request, password_form.user)  # Mantener la sesión activa
                mensaje_exito = "¡Tu contraseña ha sido cambiada exitosamente!"

        if mensaje_exito:
            messages.success(request, mensaje_exito)
            return redirect('EditarPerfil')

    return render(request, 'Users/editar_usuario.html', {
        'form': form,
        'password_form': password_form,
    })
