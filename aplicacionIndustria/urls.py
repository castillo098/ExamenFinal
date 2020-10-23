from django.urls import path
from django.conf.urls import include,url
from rest_framework import routers
from .import views

router= routers.DefaultRouter()
router.register(r'administradores',views.AdministradorViewSet)
router.register(r'industrias',views.IndustriaViewSet)
router.register(r'empleados',views.EmpleadoViewSet)
router.register(r'guardias',views.GuardiaViewSet)
router.register(r'personalLimpieza',views.PersonalLimpiezaViewSet)

urlpatterns = [
    path('',views.index,name='index'),
    url(r'^',include(router.urls)),
    url(r'^api-auth',include('rest_framework.urls', namespace='rest_framework'))
]