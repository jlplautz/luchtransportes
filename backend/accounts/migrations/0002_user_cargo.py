# Generated by Django 4.1.7 on 2023-05-05 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='cargo',
            field=models.CharField(
                choices=[('M', 'Motorista'), ('G', 'Gerente')],
                default='G',
                max_length=1,
            ),
        ),
    ]
