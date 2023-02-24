from django.db import models

# Create your models here.

class Cliente(models.Model):
    dni = models.CharField(max_length=9, primary_key = True)
    nombre = models.CharField(max_length=150, blank = False, null = False)
    fechaAlta = models.DateTimeField('Fecha Alta', blank = False, null = False)
    direccion = models.CharField(max_length=150, blank = False, null = True)
    movil = models.CharField(max_length=14, blank = False, null = True)

class Concierto(models.Model):
    nombre = models.CharField(max_length=20, primary_key = True)
    fecha = models.DateTimeField(blank = False, null = False)
    lugar = models.CharField(max_length=150, blank = False, null = False)
    precio = models.CharField(max_length=14, blank = False, null = False)
    imagen = models.ImageField(verbose_name='Imagen', upload_to='imgConciertos', null=True, blank=True)