# Generated by Django 4.1.7 on 2023-06-27 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freight', '0003_alter_freight_options_alter_freight_caminhao'),
    ]

    operations = [
        migrations.AddField(
            model_name='freight',
            name='distancia',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
