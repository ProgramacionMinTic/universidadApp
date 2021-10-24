from django.db import models

class Facultades(models.Model):
    FacultadId = models.AutoField(primary_key=True)
    FacultadNombre=models.CharField(max_length=100)

class Administrativos(models.Model):
    AdministrativoId = models.AutoField(primary_key=True)
    AdministrativoNombre = models.CharField(max_length=100)
    Facultad = models.CharField(max_length=100)
    FechaIngreso = models.DateField()
    nombreFoto = models.CharField(max_length=100)