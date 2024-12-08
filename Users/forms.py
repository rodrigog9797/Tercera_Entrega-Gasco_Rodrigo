from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}


class UserEditForm(forms.ModelForm):  # Usamos ModelForm en vez de UserChangeForm
    email = forms.EmailField(
        label="Ingrese su email:",
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'})
    )
    last_name = forms.CharField(
        label="Apellido",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'})
    )
    first_name = forms.CharField(
        label="Nombre",
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'})
    )

    # Campos de contraseña (solo si el usuario quiere cambiarlas)
    new_password1 = forms.CharField(
        label="Nueva Contraseña",
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nueva Contraseña'}),
        validators=[validate_password]
    )
    new_password2 = forms.CharField(
        label="Confirmar Nueva Contraseña",
        required=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmar Nueva Contraseña'}),
        validators=[validate_password]
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
        help_texts = {field: "" for field in fields}

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")

        # Verificar que las contraseñas coincidan si se han ingresado
        if password1 or password2:
            if password1 != password2:
                raise forms.ValidationError("Las contraseñas no coinciden.")
        
        return cleaned_data

    def save(self, commit=True):
        # Guardar el usuario sin cambios en la contraseña
        user = super().save(commit=False)
        password1 = self.cleaned_data.get("new_password1")
        
        # Si se proporcionó una nueva contraseña, actualizarla
        if password1:
            user.set_password(password1)
        
        if commit:
            user.save()
        return user
