from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Eliminar null=True
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)  # Es correcto mantener null=True y blank=True en imagen

    def __str__(self):
        return f"Avatar de {self.user.username}"
