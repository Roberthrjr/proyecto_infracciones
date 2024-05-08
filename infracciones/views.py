from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from .serializers import (
    UsuarioSerializer,
    User,
    InspectorSerializer,
    InspectorUpdateSerializer,
    InspectorModelo,
    ConductorSerializer,
    ConductorUpdateSerializer,
    ConductorModelo,
    VehiculoSerializer,
    VehiculoUpdateSerializer,
    VehiculoModelo,
    ActaSerializer,
    ActaUpdateSerializer,
    ActaModelo,
)
from django.db import transaction
from rest_framework_simplejwt.views import TokenObtainPairView
import requests
from datetime import datetime
from pprint import pprint

# Se define la vista para listar los usuarios
class UsuarioView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

# Se define la vista para crear un usuario
class UsuarioCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

# Se define la vista para actualizar un usuario
class UsuarioUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

# Se define la vista para eliminar un usuario
class UsuarioDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
    # Se define el metodo destroy para manejar la solicitud de eliminacion de un objeto usuario
    def destroy(self, request, *args, **kwargs):
        try:
            # Obtenemos el objeto usuario a eliminar
            instance = self.get_object()
            # Actualizamos el estado del usuario a "Inactivo"
            instance.is_active = False
            # Guardamos los cambios en la base de datos
            instance.save()
            # Retornamos una respuesta exitosa
            return Response({'mensaje':'Usuario eliminado correctamente'},status=status.HTTP_200_OK)
        except Exception as e:
            # Retornamos una respuesta de error en caso de que ocurra un error
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
 
# Se define la vista para listar los inspectores
class IspectorView(generics.ListAPIView):
    queryset = InspectorModelo.objects.all()
    serializer_class = InspectorSerializer

# Se define la vista para crear un inspector
class InspectorCreateView(generics.CreateAPIView):
    queryset = InspectorModelo.objects.all()
    serializer_class = InspectorSerializer
    
# Se define la vista para actualizar un inspector
class InspectorUpdateView(generics.UpdateAPIView):
    queryset = InspectorModelo.objects.all()
    serializer_class = InspectorUpdateSerializer

# Se define la vista para eliminar un inspector
class InspectorDeleteView(generics.DestroyAPIView):
    queryset = InspectorModelo.objects.all()
    serializer_class = InspectorSerializer
    
    # Se define el metodo destroy para manejar la solicitud de eliminacion de un objeto inspector
    def destroy(self, request, *args, **kwargs):
        try:
            # Obtenemos el objeto inspector a eliminar
            instance = self.get_object()
            # Actualizamos el estado del inspector a "Inactivo"
            instance.estado = "Inactivo"
            # Guardamos los cambios en la base de datos
            instance.save()
            # Retornamos una respuesta exitosa
            return Response({'mensaje':'Inspector eliminado correctamente'},status=status.HTTP_200_OK)
        except Exception as e:
            # Retornamos una respuesta de error en caso de que ocurra un error
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# Se define la vista para listar los conductores
class ConductorView(generics.ListAPIView):
    queryset = ConductorModelo.objects.all()
    serializer_class = ConductorSerializer

# Se define la vista para crear un conductor
class ConductorCreateView(generics.CreateAPIView):
    queryset = ConductorModelo.objects.all()
    serializer_class = ConductorSerializer

# Se define la vista para actualizar un conductor
class ConductorUpdateView(generics.UpdateAPIView):
    queryset = ConductorModelo.objects.all()
    serializer_class = ConductorUpdateSerializer

# Se define la vista para eliminar un conductor
class ConductorDeleteView(generics.DestroyAPIView):
    queryset = ConductorModelo.objects.all()
    serializer_class = ConductorSerializer
    
    # Se define el metodo destroy para manejar la solicitud de eliminacion de un objeto conductor
    def destroy(self, request, *args, **kwargs):
        try:
            # Obtenemos el objeto conductor a eliminar
            instance = self.get_object()
            # Actualizamos el estado del conductor a "Inactivo"
            instance.estado = "Inactivo"
            # Guardamos los cambios en la base de datos
            instance.save()
            # Retornamos una respuesta exitosa
            return Response({'mensaje':'Conductor eliminado correctamente'}, status=status.HTTP_200_OK)
        except Exception as e:
            # Retornamos una respuesta de error en caso de que ocurra un error
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Se define la vista para listar los vehiculos
class VehiculoView(generics.ListAPIView):
    queryset = VehiculoModelo.objects.all()
    serializer_class = VehiculoSerializer

# Se define la vista para crear un vehiculo
class VehiculoCreateView(generics.CreateAPIView):
    queryset = VehiculoModelo.objects.all()
    serializer_class = VehiculoSerializer

# Se define la vista para actualizar un vehiculo
class VehiculoUpdateView(generics.UpdateAPIView):
    queryset = VehiculoModelo.objects.all()
    serializer_class = VehiculoUpdateSerializer

# Se define la vista para eliminar un vehiculo
class VehiculoDeleteView(generics.DestroyAPIView):
    queryset = VehiculoModelo.objects.all()
    serializer_class = VehiculoSerializer

# Se define la vista para listar los actas
class ActaView(generics.ListAPIView):
    queryset = ActaModelo.objects.all()
    serializer_class = ActaSerializer

# Se define la vista para crear un acta
class ActaCreateView(generics.CreateAPIView):
    queryset = ActaModelo.objects.all()
    serializer_class = ActaSerializer

# Se define la vista para actualizar un acta
class ActaUpdateView(generics.UpdateAPIView):
    queryset = ActaModelo.objects.all()
    serializer_class = ActaUpdateSerializer

# Se define la vista para eliminar un acta
class ActaDeleteView(generics.DestroyAPIView):
    queryset = ActaModelo.objects.all()
    serializer_class = ActaSerializer
    
    # Se define el metodo destroy para manejar la solicitud de eliminacion de un objeto acta
    def destroy(self, request, *args, **kwargs):
        try:
            # Obtenemos el objeto acta a eliminar
            instance = self.get_object()
            # Actualizamos el estado del acta a "Inactivo"
            instance.estado = "Rechazado"
            # Guardamos los cambios en la base de datos
            instance.save()
            # Retornamos una respuesta exitosa
            return Response({'mensaje':'Acta eliminada correctamente'}, status=status.HTTP_200_OK)
        except Exception as e:
            # Retornamos una respuesta de error en caso de que ocurra un error
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)