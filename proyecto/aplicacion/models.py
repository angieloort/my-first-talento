from django.db import models


class Persona(models.Model):
    identificacion = models.CharField(max_length=100)
    nombre_apellidos = models.CharField(max_length=100)
    area = models.CharField(max_length=80)
    cargo = models.CharField(max_length=80)
