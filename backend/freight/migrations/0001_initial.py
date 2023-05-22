# Generated by Django 4.1.7 on 2023-05-18 21:13
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
        ('truck', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Freight',
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
                ('data', models.DateField(auto_now_add=True)),
                (
                    'origem',
                    models.CharField(max_length=30, verbose_name='Origem'),
                ),
                (
                    'destino',
                    models.CharField(max_length=30, verbose_name='Destino'),
                ),
                (
                    'pedagio_pgto',
                    models.CharField(
                        choices=[('SP', 'Sem_parar'), ('DN', 'Dinheiro')],
                        default='SP',
                        max_length=2,
                    ),
                ),
                ('pedagio_valor', models.CharField(max_length=10)),
                ('frete_adiant_valor', models.CharField(max_length=10)),
                ('frete_saldo_valor', models.CharField(max_length=10)),
                (
                    'frete_status',
                    models.CharField(
                        choices=[('PG', 'Pago'), ('FS', 'Falta_Saldo')],
                        default='FS',
                        max_length=2,
                    ),
                ),
                (
                    'caminhao',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to='truck.truck',
                    ),
                ),
                (
                    'motorista',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to='driver.driver',
                    ),
                ),
            ],
        ),
    ]
