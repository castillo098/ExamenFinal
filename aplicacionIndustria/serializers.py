from aplicacionIndustria.models import Administrador,Industria,Empleado,Guardia,PersonalLimpieza
from rest_framework import serializers

class AdministradorSerializer(serializers.ModelSerializer):
    class Meta: 
        model=Administrador
        fields=('idAministrador','Cedula','Nombre','Apellido','Edad','Telefono','Email','Direccion','Ciudad','Estudios')
class IndustriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Industria
        fields=('idAdmisnitrador','idIndustria','Nombre','Direccion','Ciudad','Telefono')
class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields=('idEmpleado','Ocupacion')
class GuardiaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guardia
        fields=('idGuardia','Ocupacion')
class PersonalLimpiezaSerializer(serializers.ModelSerializer):
    class Meta:
        model=PersonalLimpieza
        fields=('idPersonal','Ocupacion')
