from django.db import models


class Clientes(models.Model):
    nombre = models.CharField(max_length=40)
    numero = models.IntegerField()
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()

class Proveedores(models.Model):
    nombre = models.CharField(max_length=40)
    direccion = models.CharField(max_length=40)
    email = models.EmailField()

class Compras(models.Model):
    fecha = models.DateField()
    monto = models.IntegerField()
