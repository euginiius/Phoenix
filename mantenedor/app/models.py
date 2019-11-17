from django.db import models
from django.utils import timezone
# Create your models here.

class Producto(models.Model):
    codigo= models.IntegerField()
    nombre= models.CharField(max_length=30)
    precio= models.IntegerField()
    marca= models.CharField(max_length=20)
    modelo= models.CharField(max_length=20)
    descripcion= models.CharField(max_length=250)
    stock= models.IntegerField()

    def __str__(self):
        return self.nombre

class DatosCliente(models.Model):
    region= models.TextField()
    comuna= models.TextField()
    nombre_cliente= models.CharField(max_length=250)
    email= models.CharField(max_length=100)
    telefono= models.CharField(max_length=13)
    tipo_vivienda= models.TextField()

    def __str__(self):
        return self.nombre_cliente
