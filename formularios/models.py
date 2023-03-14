from django.db import models

# Create your models here.
class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre + self.apellido + self.cargo

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    valor = models.IntegerField()
    
    def __str__(self):
        return self.nombre + self.valor
    
class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre + self.apellido

