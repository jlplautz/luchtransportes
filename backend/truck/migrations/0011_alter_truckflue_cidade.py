# Generated by Django 4.1.7 on 2023-09-06 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('truck', '0010_truckflue_cidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truckflue',
            name='cidade',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
