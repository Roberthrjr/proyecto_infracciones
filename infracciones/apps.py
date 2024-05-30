# Importamos la clase AppConfig del módulo django.apps
from django.apps import AppConfig

# Definimos una nueva clase de configuración para la aplicación "infracciones"
class InfraccionesConfig(AppConfig):
    # Establecemos el tipo de campo automático predeterminado para los modelos de esta aplicación
    default_auto_field = 'django.db.models.BigAutoField'
    # Nombre de la aplicación
    name = 'infracciones'
