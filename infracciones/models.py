# Importamos el modulo models
from django.db import models

# Creamos el modelo Inspector
class InspectorModelo(models.Model):
    # Creamos las columnas de la tabla
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=20)
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    
    # Creamos el nombre de la tabla
    class Meta:
        db_table = 'inspectores'
    
    # Creamos el metodo para mostrar el nombre completo del inspector
    def __str__(self):
        return self.nombres + ' ' + self.apellidos

# Creamos el modelo Conductor
class ConductorModelo(models.Model):
    # Creamos las columnas de la tabla
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_documento = models.CharField(max_length=20)
    numero_documento = models.CharField(max_length=20)
    codigo_licencia = models.CharField(max_length=20)
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)
    
    # Creamos el nombre de la tabla
    class Meta:
        db_table = 'conductores'
    
    # Creamos el metodo para mostrar el nombre completo del conductor
    def __str__(self):
        return self.nombres + ' ' + self.apellidos

# Creamos el modelo Vehiculo
class VehiculoModelo(models.Model):
    # Creamos las columnas de la tabla
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=20)
    color = models.CharField(max_length=50)
    clase = models.CharField(max_length=50)
    anio_fabricacion = models.IntegerField()
    
    # Creamos el nombre de la tabla
    class Meta:
        db_table = 'vehiculos'
    
    # Creamos el metodo para mostrar la marca y el modelo del vehiculo
    def __str__(self):
        return self.marca + ' ' + self.modelo

# Creamos el modelo Acta
class ActaModelo(models.Model):
    # Creamos las columnas de la tabla
    fecha = models.DateField()
    conductor = models.ForeignKey(ConductorModelo, on_delete=models.CASCADE)
    vehiculo = models.ForeignKey(VehiculoModelo, on_delete=models.CASCADE)
    inspector = models.ForeignKey(InspectorModelo, on_delete=models.CASCADE)
    lugar = models.CharField(max_length=200)
    hora = models.TimeField()
    observaciones = models.TextField()
    CALIFICACION_CHOICES = [
        ('Leve', 'Leve'),
        ('Grave', 'Grave'),
        ('Muy Grave', 'Muy Grave'),
    ]
    calificacion = models.CharField(max_length=20, choices=CALIFICACION_CHOICES)
    sancion = models.TextField()
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Aprobado', 'Aprobado'),
        ('Rechazado', 'Rechazado'),
    ]
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)