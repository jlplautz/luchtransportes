# Generated by Django 4.1.7 on 2023-07-06 18:37
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0006_alter_truckflue_litros'),
        ('freight', '0004_freight_distancia'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreightFee',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('contrato', models.CharField(max_length=15)),
                ('cod_operacao', models.CharField(max_length=15)),
                ('data', models.DateField()),
                (
                    'valor_adiant_fixo',
                    models.DecimalField(decimal_places=2, max_digits=7),
                ),
                (
                    'valor_saldo_fixo',
                    models.DecimalField(decimal_places=2, max_digits=7),
                ),
                (
                    'valor_desc_fixo',
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7
                    ),
                ),
                (
                    'frete_status',
                    models.CharField(
                        blank=True,
                        choices=[('PG', 'Pago'), ('FS', 'Falta_Saldo')],
                        default='FS',
                        max_length=2,
                    ),
                ),
                (
                    'caminhao',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='freightfees',
                        to='truck.truck',
                        verbose_name='caminhao',
                    ),
                ),
            ],
            options={
                'verbose_name': 'freightfee',
                'verbose_name_plural': 'freightfees',
                'ordering': ('data',),
            },
        ),
    ]