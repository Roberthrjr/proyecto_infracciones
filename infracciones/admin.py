# Importamos el módulo de administración de Django
from django.contrib import admin

# Importamos los modelos definidos en el archivo models.py del mismo directorio
from .models import (
    InspectorModelo,
    ConductorModelo,
    VehiculoModelo,
    ActaModelo
)

# Registramos los modelos en el sitio de administración de Django
# Esto permite gestionar instancias de los modelos a través de la interfaz de administración
admin.site.register(InspectorModelo)
admin.site.register(ConductorModelo)
admin.site.register(VehiculoModelo)
admin.site.register(ActaModelo)