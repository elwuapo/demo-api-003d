from django.db import models

# Create your models here.

class Fabricante(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)

class Componente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=99)
    fabricante = models.ForeignKey(Fabricante, on_delete=models.CASCADE, null=True, blank=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    def ruta(self,  filename):
        return f'Productos/ {self.id}/{filename}'

    imgen = models.ImageField(upload_to = ruta, null=True, blank=True)
