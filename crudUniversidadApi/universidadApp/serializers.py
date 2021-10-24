from rest_framework import serializers
from universidadApp.models import Facultades, Administrativos

class FacultadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Facultades
        fields=('FacultadId', 'FacultadNombre')

class AdministrativoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Administrativos
        fields=('AdministrativoId', 'AdministrativoNombre', 'Facultad', 'FechaIngreso', 'nombreFoto')