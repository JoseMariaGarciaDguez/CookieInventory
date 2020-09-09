from django.db import models
from django.contrib.auth.models import AbstractUser


class Categoria(models.Model):
    categoria_nombre = models.CharField(max_length=30)
    categoria_descripcion = models.TextField(max_length=200)
    categoria_imagen = models.ImageField(upload_to='categorias', default='none/nulo.png')

    def __str__(self):
        return self.categoria_nombre


class Producto(models.Model):
    producto_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    producto_nombre = models.CharField(max_length=30)
    producto_descripcion = models.TextField(max_length=200)
    producto_stock = models.IntegerField()
    producto_imagen = models.ImageField(upload_to='productos', default='none/nulo.png')

    def __str__(self):
        return self.producto_nombre


class UserProfile(AbstractUser):
    fecha_de_nacimiento = models.DateField(null=True, blank=True)
    ciudad_de_nacimiento = models.CharField(max_length=30)
    foto = models.ImageField(upload_to='perfiles', default='none/sin-foto.jpg')

