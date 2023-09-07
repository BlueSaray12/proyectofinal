from django.db import models

# Create your models here.
class Redes(models.Model):
    key=models.SlugField(verbose_name='Clave nombre', max_length=60, unique=True)
    name=models.CharField(max_length=60, verbose_name='Red Social')
    url=models.URLField(verbose_name='Enlace de la red social', null=True, blank=True)
    create=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name='Red Social'
        verbose_name_plural='Redes Sociales'
        ordering=['name']

    def __str__(self):
        return self.name

