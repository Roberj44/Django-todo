from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tareas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"

    def __str__(self):
        return self.titulo