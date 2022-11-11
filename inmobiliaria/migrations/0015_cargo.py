# Generated by Django 3.2.3 on 2022-11-11 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmobiliaria', '0014_remove_departamento_activo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('nombre', models.CharField(max_length=250, verbose_name='Nombre')),
                ('actividad', models.CharField(max_length=500, verbose_name='Actividad')),
            ],
        ),
    ]