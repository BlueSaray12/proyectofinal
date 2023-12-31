# Generated by Django 4.2.4 on 2023-09-07 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre del Chef')),
                ('designation', models.TextField(verbose_name='Rol del Equipo')),
                ('image', models.ImageField(upload_to='projects', verbose_name='Fotografía')),
                ('create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')),
            ],
            options={
                'verbose_name': 'Proyecto',
                'verbose_name_plural': 'Proyectos',
                'ordering': ['-create'],
            },
        ),
    ]
