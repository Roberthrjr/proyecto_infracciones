# Importamos el modelo de usuarios
from django.contrib.auth.models import User
# Importamos la clase serializers de DRF
from rest_framework import serializers
# Importamos los modelos
from .models import (
    InspectorModelo,
    ConductorModelo,
    VehiculoModelo,
    ActaModelo
)
# Importamos los serializers de JWT
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Se define el serializer para el modelo usuarios
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        
        return user
    
    def to_representation(self, instance):
        return super().to_representation(instance)

# Se define el serializer para el token
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    
    def token(cls, user):
        token = super().token(user)
        token['email'] = user.email
        return token

# Se define el serializer para el modelo inspector
class InspectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InspectorModelo
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation

# Se define el serializer para actualizar el modelo inspector
class InspectorUpdateSerializer(serializers.ModelSerializer):
    # Campos opcionales
    nombres = serializers.CharField(required=False)
    apellidos = serializers.CharField(required=False)
    foto = serializers.CharField(required=False)
    tipo_documento = serializers.CharField(required=False)
    numero_documento = serializers.CharField(required=False)
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = serializers.ChoiceField(choices=ESTADO_CHOICES, required=False)
    
    class Meta:
        model = InspectorModelo
        fields = '__all__'

# Se define el serializer para el modelo conductor
class ConductorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConductorModelo
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['foto'] = instance.foto.url
        return representation
    
# Se define el serializer para actualizar el modelo conductor
class ConductorUpdateSerializer(serializers.ModelSerializer):
    # Campos opcionales
    nombres = serializers.CharField(required=False)
    apellidos = serializers.CharField(required=False)
    foto = serializers.CharField(required=False)
    tipo_documento = serializers.CharField(required=False)
    numero_documento = serializers.CharField(required=False)
    codigo_licencia = serializers.CharField(required=False)
    ESTADO_CHOICES = [
        ('Activo', 'Activo'),
        ('Inactivo', 'Inactivo'),
    ]
    estado = serializers.ChoiceField(choices=ESTADO_CHOICES, required=False)

    class Meta:
        model = ConductorModelo
        fields = '__all__'

# Se define el serializer para el modelo vehiculo
class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehiculoModelo
        fields = '__all__'

    def to_representation(self, instance):
        return super().to_representation(instance)

# Se define el serializer para actualizar el modelo vehiculo
class VehiculoUpdateSerializer(serializers.ModelSerializer):
    # Campos opcionales
    marca = serializers.CharField(required=False)
    modelo = serializers.CharField(required=False)
    placa = serializers.CharField(required=False)
    color = serializers.CharField(required=False)
    clase = serializers.CharField(required=False)
    anio_fabricacion = serializers.IntegerField(required=False)

    class Meta:
        model = VehiculoModelo
        fields = '__all__'

# Se define el serializer para el modelo acta
class ActaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActaModelo
        fields = '__all__'

    def to_representation(self, instance):
        return super().to_representation(instance)

# Se define el serializer para actualizar el modelo acta
class ActaUpdateSerializer(serializers.ModelSerializer):
    # Campos opcionales
    fecha = serializers.DateField(required=False)
    conductor = serializers.CharField(required=False)
    vehiculo = serializers.CharField(required=False)
    inspector = serializers.CharField(required=False)
    lugar = serializers.CharField(required=False)
    hora = serializers.TimeField(required=False)
    observaciones = serializers.CharField(required=False)
    CALIFICACION_CHOICES = [
        ('Leve', 'Leve'),
        ('Grave', 'Grave'),
        ('Muy grave', 'Muy grave')
    ]
    calificacion = serializers.ChoiceField(choices=CALIFICACION_CHOICES, required=False)
    sancion = serializers.CharField(required=False)
    ESTADO_CHOICES = [
        ('Pendiente', 'Pendiente'),
        ('Concluido', 'Concluido'),
    ]
    estado = serializers.ChoiceField(choices=ESTADO_CHOICES, required=False)
    
    class Meta:
        model = ActaModelo
        fields = '__all__'