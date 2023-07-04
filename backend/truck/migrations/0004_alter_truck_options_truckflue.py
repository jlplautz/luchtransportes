# Generated by Django 4.1.7 on 2023-06-27 18:51
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0003_delete_truckfees'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='truck',
            options={
                'ordering': ('placa',),
                'verbose_name': 'truck',
                'verbose_name_plural': 'trucks',
            },
        ),
        migrations.CreateModel(
            name='TruckFlue',
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
                ('data', models.DateField()),
                (
                    'flue_valor',
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=7,
                    ),
                ),
                ('km_atual', models.IntegerField(default=0)),
                (
                    'caminhao',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name='truck',
                        to='truck.truck',
                        verbose_name='caminhao',
                    ),
                ),
            ],
            options={
                'verbose_name': 'truckflue',
                'verbose_name_plural': 'truckflues',
                'ordering': ('data',),
            },
        ),
    ]
