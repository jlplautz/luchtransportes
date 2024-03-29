# Generated by Django 4.1.7 on 2023-08-08 21:08
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('driver', '0002_alter_driver_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={
                'ordering': ('motorista',),
                'verbose_name': 'driver',
                'verbose_name_plural': 'drivers',
            },
        ),
        migrations.RemoveField(
            model_name='driver',
            name='email',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='nome',
        ),
        migrations.AddField(
            model_name='driver',
            name='motorista',
            field=models.OneToOneField(
                max_length=3,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name='drivers',
                to=settings.AUTH_USER_MODEL,
                verbose_name='motorista',
            ),
        ),
    ]
