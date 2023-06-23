from django.db import models
from django.urls import reverse_lazy

from backend.driver.models import Driver
from backend.truck.models import Truck


class Freight(models.Model):
    choices_pedagio = (('SP', 'Sem_parar'), ('DN', 'Dinheiro'))
    choices_frete = (('PG', 'Pago'), ('FS', 'Falta_Saldo'))
    contrato = models.CharField(max_length=15)
    cod_operacao = models.CharField(max_length=15)
    data = models.DateField()
    caminhao = models.ForeignKey(
        Truck,
        related_name='freights',
        verbose_name='caminhao',
        on_delete=models.DO_NOTHING,
    )
    motorista = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    origem = models.CharField(max_length=30, verbose_name='Origem')
    km_origem = models.IntegerField(default=0)
    destino = models.CharField(max_length=30, verbose_name='Destino')
    km_destino = models.IntegerField(default=0)
    pedagio_pgto = models.CharField(
        max_length=2,
        choices=choices_pedagio,
        default='SP',
    )
    pedagio_valor = models.DecimalField(
        max_digits=5,
        decimal_places=2,
    )
    frete_adiant_valor = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    frete_saldo_valor = models.DecimalField(
        max_digits=7,
        decimal_places=2,
    )
    frete_desc_valor = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        blank=True,
    )
    frete_status = models.CharField(
        max_length=2,
        choices=choices_frete,
        default='FS',
    )

    class Meta:
        ordering = ('data',)
        verbose_name = 'freight'
        verbose_name_plural = 'freights'

    def __str__(self):
        return self.origem

    def list_url(self):
        return reverse_lazy('freight:freight_list')

    @property
    def verbose_name(self):
        return self._meta.verbose_name

    @property
    def verbose_name_plural(self):
        return self._meta.verbose_name_plural
