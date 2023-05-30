from django.db import models

from backend.driver.models import Driver
from backend.truck.models import Truck

# class Cidade(models.Model):
#     choices_estado = (('SC', 'Santa-Catarina'), ('SP', 'São Paulo'))
#     estado = models.CharField(max_length=2, choices=choices_estado)
#     cidade = models.CharField(max_length=15)

#     def __str__(self):
#         return self.estado-self.cidade


class Freight(models.Model):
    choices_pedagio = (('SP', 'Sem_parar'), ('DN', 'Dinheiro'))
    choices_frete = (('PG', 'Pago'), ('FS', 'Falta_Saldo'))
    contrato = models.CharField(max_length=15)
    cod_operacao = models.CharField(max_length=15)
    data = models.DateField()
    caminhao = models.ForeignKey(Truck, on_delete=models.DO_NOTHING)
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

    def __str__(self):
        return self.origem
