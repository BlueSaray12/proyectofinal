from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=50, verbose_name='Nombre del Chef')
    designation=models.TextField(verbose_name='Rol del Equipo')
    image=models.ImageField(verbose_name='Fotografía', upload_to='projects')
    create=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')


    class Meta:
        verbose_name='Equipo'
        verbose_name_plural='Equipos de Chefs'
        ordering=['-create']

    def __str__(self):
        return self.name

