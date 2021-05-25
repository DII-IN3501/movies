from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    estreno = models.DateField(null=True)
    genero = models.CharField(max_length=255)
    idioma = models.CharField(max_length=7)

    def __str__(self):
        return self.titulo

class Subtitulo(models.Model):
    idioma = models.CharField(max_length=7)
    contenido = models.FileField(upload_to="uploads/")
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)

class Persona(models.Model):
    nombre = models.CharField(max_length=255)
    nacionalidad = models.CharField(max_length=255)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

class Participacion(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=255)
