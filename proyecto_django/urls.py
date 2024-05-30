# Importamos los módulos necesarios de Django y otras bibliotecas
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

# Importamos los módulos necesarios para la documentación de la API con drf_yasg
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

# Configuramos la vista del esquema de la API utilizando drf_yasg
schema_view = get_schema_view(
   openapi.Info(
      title="Infracciones API", # Título de la documentación de la API
      default_version='v1', # Versión de la API
      description="API para la gestion de actas de transito", # Descripción de la API
      contact=openapi.Contact(email="tauroroberth00@gmail.com"), # Información de contacto
      license=openapi.License(name="BSD License"), # Licencia de la API
   ),
   public=True, # Indica si el esquema es público
   permission_classes=(permissions.AllowAny,), # Permisos para acceder a la documentación
)

# Definimos las URL de la aplicación
urlpatterns = [
   # Redirige la URL raíz al visor de Swagger
    path('', RedirectView.as_view(url='swagger/')),
    # URL para obtener el esquema de la API en formato JSON o YAML
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    # URL para el visor de Swagger UI
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # URL para el visor de Redoc
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # URL para acceder al sitio de administración de Django
    path('admin/', admin.site.urls),
    # Incluye las URLs definidas en la aplicación 'infracciones'
    path('api/', include('infracciones.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # Añade soporte para servir archivos estáticos en desarrollo
