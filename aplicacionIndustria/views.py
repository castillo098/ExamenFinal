from django.shortcuts import render
from django.http import HttpResponse
from aplicacionIndustria.models import Administrador, Industria, Empleado, Guardia,PersonalLimpieza
from rest_framework import viewsets
from aplicacionIndustria.serializers import AdministradorSerializer, IndustriaSerializer,EmpleadoSerializer, GuardiaSerializer, PersonalLimpiezaSerializer

#Insertar vistas
class AdministradorViewSet(viewsets.ModelViewSet):
    queryset=Administrador.objects.all().order_by('idAdministrador')
    serializer_class=AdministradorSerializer

class IndustriaViewSet(viewsets.ModelViewSet):
    queryset=Industria.objects.all().order_by('IdIndustria')
    serializer_class= IndustriaSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset=Empleado.objects.all().order_by('idEmpleado')
    serializer_class=EmpleadoSerializer

class GuardiaViewSet(viewsets.ModelViewSet):
    queryset=Guardia.objects.all().order_by('idGuardia')
    serializer_class=GuardiaSerializer

class PersonalLimpiezaViewSet(viewsets.ModelViewSet):
    queryset=PersonalLimpieza.objects.all().order_by('idPersonal')
    serializer_class=PersonalLimpiezaSerializer

def index(request):
    return HttpResponse("Aplicacion realizada de Indistrias Culturales")
