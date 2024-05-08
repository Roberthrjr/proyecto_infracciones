from django.contrib import admin
from .models import (
    InspectorModelo,
    ConductorModelo,
    VehiculoModelo,
    ActaModelo
)

admin.site.register(InspectorModelo)
admin.site.register(ConductorModelo)
admin.site.register(VehiculoModelo)
admin.site.register(ActaModelo)