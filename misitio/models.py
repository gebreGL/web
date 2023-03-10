from django.core.validators import FileExtensionValidator
from django.db import models

# Create your models here.

# class Cliente(models.Model):
#     usuario = models.CharField(max_length=150, blank = False, null = False)
#
#     fechaAlta = models.DateTimeField('Fecha Alta', blank = False, null = False)
#     direccion = models.CharField(max_length=150, blank = False, null = True)
#     movil = models.CharField(max_length=14, blank = False, null = True)

class Concierto(models.Model):
    nombre = models.CharField(max_length=100, primary_key = True)
    fecha = models.DateField(blank = False, null = False)
    lugar = models.CharField(max_length=150, blank = False, null = False)
    precio = models.CharField(max_length=14, blank = False, null = False)
    imagen = models.ImageField(upload_to='uploads/', null=True, validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png'])])