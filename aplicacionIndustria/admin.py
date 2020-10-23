from django.contrib import admin
from .models import Administrador
from .models import Industria
from .models import Empleado
from .models import Guardia
from .models import PersonalLimpieza

# Register your models here.
admin .site.register(Administrador)
admin .site.register(Industria)
admin .site.register(Empleado)
admin .site.register(Guardia)
admin .site.register(PersonalLimpieza)

