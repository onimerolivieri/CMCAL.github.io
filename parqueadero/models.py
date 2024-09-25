from django.db import models
from django.contrib.auth.models import User

# Modelo Vehiculo
class Vehiculo(models.Model):
    propietario = models.CharField(max_length=100)
    placas = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    color = models.CharField(max_length=30)
    esta_autorizado = models.BooleanField(default=False)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.marca} - {self.placas}'

# Modelo Funcionario
class Funcionario(models.Model):
    nombre = models.CharField(max_length=100)
    lugar_trabajo = models.CharField(max_length=100)
    cargo = models.CharField(max_length=50)  # Ejemplo de otro detalle relevante
    documento = models.CharField(max_length=20, unique=True)  # Añadir identificación única

    def __str__(self):
        return self.nombre

# Modelo ControlIngreso
class ControlIngreso(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    registrado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.vehiculo} ingresó el {self.fecha_ingreso}'

# Modelo Autorizaciones
class Autorizacion(models.Model):
    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    empresa = models.CharField(max_length=100)
    trabajo_a_realizar = models.TextField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    lugar_trabajo = models.CharField(max_length=100)
    autorizado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Para saber quién autorizó

    def __str__(self):
        return f'{self.nombre} - {self.empresa}'
