from django.db import models


class Truck(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    ano_fab = models.PositiveIntegerField()
    placa = models.CharField(max_length=10)
    Chassis = models.CharField(max_length=20)
    odometro = models.PositiveIntegerField()

    def __str__(self):
        return self.placa
