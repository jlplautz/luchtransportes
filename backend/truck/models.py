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


# class TruckFees(models.Model):
#     choices_fixo = (('PG', 'Pago'), ('FS', 'Falta_Saldo'))
#     contrato = models.CharField(max_length=15)
#     cod_operacao = models.CharField(max_length=15)
#     data = models.DateField()
#     caminhao = models.ForeignKey(Truck, on_delete=models.DO_NOTHING)
#     valor_adiant_fixo = models.DecimalField(
#         max_digits=7,
#         decimal_places=2,
#     )
#     valor_saldo_fixo = models.DecimalField(
#         max_digits=7,
#         decimal_places=2,
#     )
#     valor_desc_fixo = models.DecimalField(
#         max_digits=7,
#         decimal_places=2,
#         blank=True,
#     )
#     status_fixo = models.CharField(
#         max_length=2,
#         choices=choices_fixo,
#         default='FS',
#     )
