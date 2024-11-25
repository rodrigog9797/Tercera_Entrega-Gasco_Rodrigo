from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=30)
    descripcion_categoria = models.TextField(blank=True, null=True)

    #def __str__(self):
        #return self.name

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200)
    descripcion_producto = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    categorias = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="products")
    imagen = models.ImageField(upload_to='imagen_producto/', blank=True, null=True)
    
    #def __str__(self):
        #return self.name
    
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    telefono = models.CharField (max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return (f"{self.nombre} {self.apellido}")
    


