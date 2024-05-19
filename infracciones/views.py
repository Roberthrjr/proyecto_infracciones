from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated
from .serializers import (
    MyTokenObtainPairSerializer,
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
from cloudinary.uploader import upload
from rest_framework_simplejwt.views import TokenObtainPairView

# Se define la vista para listar los usuarios
class UsuarioView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

# Se define la vista para crear un usuario
class UsuarioCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer
    
    # Se define el metodo post
    def post(self, request, *args, **kwargs):
        try:
            email = request.data.get('email')
            usuario= User.objects.filter(email=email).first()
            if usuario:
                return Response({'mensaje': 'El usuario ya existe'}, status=status.HTTP_400_BAD_REQUEST)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            nuevoUsuario = serializer.save()
            response = self.serializer_class(nuevoUsuario).data
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Se define la vista para iniciar sesion
class UsuarioLoginView(TokenObtainPairView):
    queryset = User.objects.all()
    serializer_class = MyTokenObtainPairSerializer

# Se define la vista para actualizar un usuario
class UsuarioUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UsuarioSerializer

# Se define la vista para eliminar un usuario
class UsuarioDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]
    queryset = InspectorModelo.objects.all()
    serializer_class = InspectorSerializer
    
# Se define la vista para actualizar un inspector
class InspectorUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = InspectorModelo.objects.all()
    serializer_class = InspectorUpdateSerializer

# Se define la vista para eliminar un inspector
class InspectorDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
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

# Se define la vista para subir una foto de un inspector
class InspectorUploadFotoView(generics.GenericAPIView):
    # Se define la lista de permisos para esta vista
    permission_classes = [IsAuthenticated]
    # Se define el queryset para esta vista
    serializer_class = InspectorSerializer

    # Se define el metodo post
    def post(self, request: Request):
        try:
            # Obtenemos la foto del inspector
            foto = request.FILES.get('foto')
            # Validamos que la foto no sea nula
            if not foto:
                raise ValueError("No se ha encontrado la foto")
            # Subimos la foto al servidor de Cloudinary
            uploadFoto = upload(foto)
            # Obtenemos el nombre de la foto
            nombreFoto = uploadFoto['secure_url'].split('/')[-1]
            # Creamos la ruta de la foto
            rutaFoto = f'{uploadFoto["resource_type"]}/{uploadFoto["type"]}/v{uploadFoto["version"]}/{nombreFoto}'
            # Actualizamos la foto del inspector
            return Response({'url': rutaFoto}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
# Se define la vista para listar los conductores
class ConductorView(generics.ListAPIView):
    queryset = ConductorModelo.objects.all()
    serializer_class = ConductorSerializer

# Se define la vista para crear un conductor
class ConductorCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ConductorModelo.objects.all()
    serializer_class = ConductorSerializer
    
# Se define la vista para actualizar un conductor
class ConductorUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ConductorModelo.objects.all()
    serializer_class = ConductorUpdateSerializer

# Se define la vista para eliminar un conductor
class ConductorDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
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

# Se define la vista para subir una foto de un conductor
class ConductorUploadFotoView(generics.GenericAPIView):
    # Se define la lista de permisos para esta vista
    permission_classes = [IsAuthenticated]
    # Se define el queryset para esta vista
    serializer_class = ConductorSerializer

    # Se define el metodo post
    def post(self, request: Request):
        try:
            # Obtenemos la foto del conductor
            foto = request.FILES.get('foto')
            # Validamos que la foto no sea nula
            if not foto:
                raise ValueError("No se ha encontrado la foto")
            # Subimos la foto al servidor de Cloudinary
            uploadFoto = upload(foto)
            # Obtenemos el nombre de la foto
            nombreFoto = uploadFoto['secure_url'].split('/')[-1]
            # Creamos la ruta de la foto
            rutaFoto = f'{uploadFoto["resource_type"]}/{uploadFoto["type"]}/v{uploadFoto["version"]}/{nombreFoto}'
            # Actualizamos la foto del conductor
            return Response({'url': rutaFoto}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Se define la vista para listar los vehiculos
class VehiculoView(generics.ListAPIView):
    queryset = VehiculoModelo.objects.all()
    serializer_class = VehiculoSerializer

# Se define la vista para crear un vehiculo
class VehiculoCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VehiculoModelo.objects.all()
    serializer_class = VehiculoSerializer

# Se define la vista para actualizar un vehiculo
class VehiculoUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VehiculoModelo.objects.all()
    serializer_class = VehiculoUpdateSerializer

# Se define la vista para eliminar un vehiculo
class VehiculoDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = VehiculoModelo.objects.all()
    serializer_class = VehiculoSerializer

# Se define la vista para listar los actas
class ActaView(generics.ListAPIView):
    queryset = ActaModelo.objects.all()
    serializer_class = ActaSerializer

# Se define la vista para crear un acta
class ActaCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ActaSerializer
    
    # Se define el metodo create para manejar la solicitud de creacion de un objeto acta
    def create(self, request, *args, **kwargs):
        # Obtenemos los datos del acta a crear
        data = request.data
        # Obtenemos el id del inspector
        inspector_id = data.get('inspector')
        # Validamos que el inspector exista y este activo
        try:
            # Obtenemos el inspector
            inspector = InspectorModelo.objects.get(id=inspector_id)
            # Validamos que el inspector este activo
            if inspector.estado == "Inactivo":
                return Response({"error": "El inspector seleccionado se encuentra inactivo"}, status=status.HTTP_400_BAD_REQUEST)
        except InspectorModelo.DoesNotExist:
            return Response({"error": "El inspector seleccionado no existe"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Si el inspector existe y esta activo, continuamos con la creacion del acta
        serializer = ActaSerializer(data=data)
        # Validamos los datos del acta
        if serializer.is_valid():
            # Guardamos el acta en la base de datos
            serializer.save()
            # Retornamos una respuesta exitosa
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Retornamos una respuesta de error en caso de que los datos del acta no sean validos
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
                
# Se define la vista para actualizar un acta
class ActaUpdateView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ActaModelo.objects.all()
    serializer_class = ActaUpdateSerializer


# Se define la vista para eliminar un acta
class ActaDeleteView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
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