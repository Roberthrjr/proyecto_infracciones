# Importamos el módulo models de Django
from django.db import models
# Importamos CloudinaryField para almacenar imágenes en Cloudinary
from cloudinary.models import CloudinaryField

# Creamos el modelo Inspector
class InspectorModelo(models.Model):
    # Definimos las columnas de la tabla con sus respectivos tipos de datos
    id = models.AutoField(primary_key=True) # Clave primaria autoincremental
    nombres = models.CharField(max_length=100) # Campo de texto para nombres
    apellidos = models.CharField(max_length=100) # Campo de texto para apellidos
    foto = CloudinaryField('foto') # Campo para almacenar imágenes en Cloudinary
    tipo_documento = models.CharField(max_length=20)  # Campo de texto para el tipo de documento
    numero_documento = models.CharField(max_length=20, unique=True) # Campo de texto para el número de documento, único
    ESTADO_CHOICES = [ # Opciones para el estado del inspector
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES) # Campo de texto para el estado con opciones predefinidas
    
    # Definimos el nombre de la tabla en la base de datos
    class Meta:
        db_table = 'inspectores'
    
    # Método para mostrar el nombre completo del inspector
    def __str__(self):
        return self.nombres + ' ' + self.apellidos

# Creamos el modelo Conductor
class ConductorModelo(models.Model):
    # Definimos las columnas de la tabla con sus respectivos tipos de datos
    id = models.AutoField(primary_key=True) # Clave primaria autoincremental
    nombres = models.CharField(max_length=100) # Campo de texto para nombres
    apellidos = models.CharField(max_length=100) # Campo de texto para apellidos
    foto = CloudinaryField('foto', default='') # Campo para almacenar imágenes en Cloudinary con valor por defecto vacío
    tipo_documento = models.CharField(max_length=20) # Campo de texto para el tipo de documento
    numero_documento = models.CharField(max_length=20, unique=True) # Campo de texto para el número de documento, único
    codigo_licencia = models.CharField(max_length=20) # Campo de texto para el código de la licencia de conducir
    ESTADO_CHOICES = [ # Opciones para el estado del conductor
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES) # Campo de texto para el estado con opciones predefinidas
    
    # Definimos el nombre de la tabla en la base de datos
    class Meta:
        db_table = 'conductores'
    
    # Método para mostrar el nombre completo del conductor
    def __str__(self):
        return self.nombres + ' ' + self.apellidos

# Creamos el modelo Vehiculo
class VehiculoModelo(models.Model):
    # Definimos las columnas de la tabla con sus respectivos tipos de datos
    id = models.AutoField(primary_key=True) # Clave primaria autoincremental
    marca = models.CharField(max_length=100) # Campo de texto para la marca del vehículo
    modelo = models.CharField(max_length=100) # Campo de texto para el modelo del vehículo
    placa = models.CharField(max_length=20, unique=True) # Campo de texto para la placa del vehículo, única
    color = models.CharField(max_length=50) # Campo de texto para el color del vehículo
    clase = models.CharField(max_length=50) # Campo de texto para la clase del vehículo
    anio_fabricacion = models.IntegerField() # Campo entero para el año de fabricación del vehículo
    
    # Definimos el nombre de la tabla en la base de datos
    class Meta:
        db_table = 'vehiculos'
    
    # Método para mostrar la marca y el modelo del vehículo
    def __str__(self):
        return self.marca + ' ' + self.modelo

# Creamos el modelo Acta
class ActaModelo(models.Model):
    # Definimos las columnas de la tabla con sus respectivos tipos de datos
    id = models.AutoField(primary_key=True) # Clave primaria autoincremental
    fecha = models.DateField() # Campo de fecha para la fecha del acta
    conductor = models.ForeignKey(ConductorModelo, on_delete=models.CASCADE) # Llave foránea hacia el modelo ConductorModelo, con eliminación en cascada
    vehiculo = models.ForeignKey(VehiculoModelo, on_delete=models.CASCADE) # Llave foránea hacia el modelo VehiculoModelo, con eliminación en cascada
    inspector = models.ForeignKey(InspectorModelo, on_delete=models.CASCADE) # Llave foránea hacia el modelo InspectorModelo, con eliminación en cascada
    lugar = models.CharField(max_length=200) # Campo de texto para el lugar del acta
    hora = models.TimeField() # Campo de tiempo para la hora del acta
    observaciones = models.TextField() # Campo de texto largo para las observaciones
    CALIFICACION_CHOICES = [ # Opciones para la calificación del acta
        ('Leve', 'Leve'),
        ('Grave', 'Grave'),
        ('Muy Grave', 'Muy Grave'),
    ]
    calificacion = models.CharField(max_length=20, choices=CALIFICACION_CHOICES) # Campo de texto para la calificación con opciones predefinidas
    sancion = models.TextField() # Campo de texto largo para la sanción
    ESTADO_CHOICES = [ # Opciones para el estado del acta
        ('Pendiente', 'Pendiente'),
        ('Concluido', 'Concluido'),
        ('Rechazado', 'Rechazado')
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES) # Campo de texto para el estado con opciones predefinidas
    
    # Definimos el nombre de la tabla en la base de datos
    class Meta:
        db_table = 'actas'
    
    # Método para mostrar el ID del acta
    def __str__(self):
        return str(self.id)