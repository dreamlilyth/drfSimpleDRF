from django.db import models

# Create your models here.
class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=150)
    rut = models.CharField(max_length=150)
    primer_nombre = models.CharField(max_length=150)
    segundo_apellido = models.CharField(max_length=150)