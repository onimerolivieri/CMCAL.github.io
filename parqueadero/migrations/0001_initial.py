# Generated by Django 5.1.1 on 2024-09-14 13:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('lugar_trabajo', models.CharField(max_length=100)),
                ('cargo', models.CharField(max_length=50)),
                ('documento', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propietario', models.CharField(max_length=100)),
                ('placas', models.CharField(max_length=10, unique=True)),
                ('marca', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=30)),
                ('esta_autorizado', models.BooleanField(default=False)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Autorizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('documento', models.CharField(max_length=20, unique=True)),
                ('empresa', models.CharField(max_length=100)),
                ('trabajo_a_realizar', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_termino', models.DateField()),
                ('lugar_trabajo', models.CharField(max_length=100)),
                ('autorizado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ControlIngreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateTimeField(auto_now_add=True)),
                ('registrado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parqueadero.vehiculo')),
            ],
        ),
    ]