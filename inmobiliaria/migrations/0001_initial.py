# Generated by Django 3.2.3 on 2022-10-19 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('identificacion', models.TextField(verbose_name='Identificación')),
                ('nombres', models.TextField(verbose_name='Nombres')),
                ('apellidos', models.TextField(verbose_name='Apellidos')),
                ('image', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('cargo', models.TextField(null=True, verbose_name='Cargo')),
            ],
        ),
    ]