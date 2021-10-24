from django.db.models import manager
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from universidadApp.models import Facultades, Administrativos
from universidadApp.serializers import FacultadSerializer, AdministrativoSerializer

from django.core.files.storage import default_storage

@csrf_exempt
def facultadApi(request, id=0):
    if request.method =='GET':
        facultades = Facultades.objects.all()
        facultades_serializer = FacultadSerializer(facultades, many=True)
        return JsonResponse(facultades_serializer.data, safe=False)

    elif request.method =='POST':
        facultad_data = JSONParser().parse(request)
        facultades_serializer= FacultadSerializer(data=facultad_data)
        if facultades_serializer.is_valid():
            facultades_serializer.save()
            return JsonResponse("Insertó con éxito", safe=False)
        return JsonResponse("Error en en la inserción", safe=False)

    elif request.method== 'PUT':
        facultad_data=JSONParser().parse(request)
        facultad = Facultades.objects.get(FacultadId = facultad_data['FacultadId'])
        facultades_serializer=FacultadSerializer(facultad, data=facultad_data)
        if facultades_serializer.is_valid():
            facultades_serializer.save()
            return JsonResponse("Actualizó con éxito", safe=False)
        return JsonResponse("Error en la actualización")

    elif request.method == 'DELETE':
        facultad = Facultades.objects.get(FacultadId=id)
        facultad.delete()
        return JsonResponse('Eliminado con éxito', safe=False)

    
@csrf_exempt
def administrativoApi(request, id=0):
    if request.method =='GET':
        administrativos = Administrativos.objects.all()
        administrativos_serializer = AdministrativoSerializer(administrativos, many=True)
        return JsonResponse(administrativos_serializer.data, safe=False)

    elif request.method =='POST':
        administrativo_data = JSONParser().parse(request)
        administrativos_serializer= AdministrativoSerializer(data=administrativo_data)
        if administrativos_serializer.is_valid():
            administrativos_serializer.save()
            return JsonResponse("Insertó con éxito", safe=False)
        return JsonResponse("Error en en la inserción", safe=False)

    elif request.method== 'PUT':
        administrativo_data=JSONParser().parse(request)
        administrativo = Administrativos.objects.get(AdministrativoId = administrativo_data['AdministrativoId'])
        administrativos_serializer=AdministrativoSerializer(administrativo, data=administrativo_data)
        if administrativos_serializer.is_valid():
            administrativos_serializer.save()
            return JsonResponse("Actualizó con éxito", safe=False)
        return JsonResponse("Error en la actualización")

    elif request.method == 'DELETE':
        administrativo = Administrativos.objects.get(AdministrativoId=id)
        administrativo.delete()
        return JsonResponse('Eliminado con éxito', safe=False)

    
@csrf_exempt
def savefile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)