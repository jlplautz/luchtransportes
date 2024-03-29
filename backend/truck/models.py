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

    class Meta:
        ordering = ('placa',)
        verbose_name = 'Truck'
        verbose_name_plural = 'Trucks'

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural


class TruckFlue(models.Model):
    caminhao = models.ForeignKey(
        Truck,
        related_name='truckflues',
        verbose_name='caminhao',
        on_delete=models.DO_NOTHING,
    )
    data = models.DateField()
    flue_valor = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    km_atual = models.IntegerField(default=0)
    litros = models.FloatField(default=0)
    descricao = models.CharField(max_length=20, default='Diesel')
    cidade = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return str(self.caminhao)

    class Meta:
        ordering = ('data',)
        verbose_name = 'TruckFlue'
        verbose_name_plural = 'TruckFlues'

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural


class TruckRepair(models.Model):
    caminhao = models.ForeignKey(
        Truck,
        related_name='truckrepairs',
        verbose_name='caminhao',
        on_delete=models.DO_NOTHING,
    )
    data = models.DateField()
    repair_valor = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    descricao = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)

    def __str__(self):
        return str(self.caminhao)

    class Meta:
        ordering = ('data',)
        verbose_name = 'truckrepair'
        verbose_name_plural = 'truckrepairs'

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural
