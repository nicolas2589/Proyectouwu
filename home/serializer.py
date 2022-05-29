from rest_framework import serializers
from django.db import models

class ClienteSerializer(serializers.Serializer):
    Nombre = models.CharField(max_length=20)
    Email = models.CharField(max_length=20)
    Phone = models.IntegerField()
