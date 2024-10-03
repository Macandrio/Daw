from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Animales(models.Model):
    Cuidador = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="Protectora")
    nombre = models.CharField(max_length = 200)
    tipo = models.CharField(max_length = 200)

    def __str__(self):
        return self.title


class protectora(models.Model):
    nombre = models.CharField(max_length = 200)
    Descripcion = models.TextField()
    Fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Colabroador(models.Model):
    nombre = models.CharField(max_length = 200)
    cargo = models.CharField(max_length = 200)
    Fecha_entrada_protectora = models.DateTimeField(default=timezone.now)

