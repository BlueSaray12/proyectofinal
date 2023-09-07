from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=100, verbose_name='Título')
    description=models.TextField(verbose_name='Descripción')
    image=models.ImageField(verbose_name='Imagen', upload_to='projects')
    author=models.ForeignKey(User, verbose_name='Autor', on_delete=models.CASCADE, null=True)
    create=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated=models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering=['-create']

    def __str__(self):
        return self.title
