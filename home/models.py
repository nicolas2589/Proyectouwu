from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class Cliente(models.Model):
    Cliente_Nombre = models.CharField(max_length=20)
    Cliente_Email = models.CharField(max_length=20)
    Cliente_Phone = models.IntegerField()

    def __str__(self):
        return "{}".format(self.Cliente_Nombre)

class Equipo(models.Model):
    Equipo_Marca = models.CharField(max_length=20)
    Equipo_Modelo = models.CharField(max_length=20)
    Equipo_SN = models.CharField(max_length=20)

    def __str__(self):
        return "{}".format(self.Equipo_SN)

class Soporte(models.Model):
    Soporte_Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Soporte_Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    Soporte_Tecnico = models.ForeignKey(User, on_delete=models.CASCADE)
    Soporte_Problema = models.CharField(max_length=30)
    Soporte_Comentarios = models.CharField(max_length=30)
    Soporte_Inicio = models.TimeField()
    Soporte_Final = models.TimeField()
    Soporte_Solucionado = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.Soporte_Problema)
