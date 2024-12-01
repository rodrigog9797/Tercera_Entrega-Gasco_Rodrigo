from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)
    descripcion_categoria = models.TextField(blank=True, null=True)

    def __str__(self):
        return (f"Nombre: {self.nombre_categoria} - Descripción: {self.descripcion_categoria}")

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200)
    descripcion_producto = models.CharField(max_length=500)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField() # Me permite saber cuantos productos tengo en stcok de cada uno
    categorias = models.CharField(max_length=30)

    def __str__(self):
        return (f"Nombre: {self.nombre_producto} - Descripción: {self.descripcion_producto} - Precio: {self.precio} - Stock: {self.stock} - Categorias: {self.categorias}")
    
    
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.CharField (max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return (f"Nombre: {self.nombre_cliente} - Apellido: {self.apellido} - Email: {self.email} - Telefono: {self.telefono} - Dirección: {self.direccion}")
    
    


