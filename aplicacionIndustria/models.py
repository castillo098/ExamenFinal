from django.db import models

# Create your models here.
class Administrador(models.Model):
    idAdministrador=models.CharField(max_length=200)
    Cedula=models.IntegerField(max_length=10)
    Nombre=models.IntegerField(max_length=200)
    Apellido=models.CharField(max_length=10)
    Edad=models.IntegerField(default=5)
    Telefono=models.CharField(max_length=10)
    Email=models.IntegerField(max_length=200)
    Direccion=models.IntegerField(max_length=200)
    Ciudad=models.IntegerField(max_length=200)
    Estudios=models.IntegerField(max_length=200)


class Industria(models.Model):
    idAdministrador=models.ForeignKey(Administrador,on_delete=models.CASCADE)
    idIndustria=models.CharField(max_length=00)
    Nombre=models.IntegerField(max_length=200)
    Direccion=models.CharField(max_length=10)
    Ciudad=models.IntegerField(max_length=10)
    Telefono=models.IntegerField(max_length=10)

class Empleado(models.model):
    idEmpleado=models.CharField(max_length=10)
    ocupacion=models.CharField(max_length=200)

class Guardia(models.model):
    idGuardia=models.CharField(max_length=10)
    ocupacion=models.CharField(max_length=200)

class PersonalLimpieza(models.Model):
    idPersonal=models.CharField(max_length=10)
    ocupacion=models.CharField(max_length=200)
