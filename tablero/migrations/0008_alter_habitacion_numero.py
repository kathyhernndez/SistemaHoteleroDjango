# Generated by Django 5.0.1 on 2024-01-29 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0007_alter_tipohabitacion_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitacion',
            name='numero',
            field=models.IntegerField(unique=True),
        ),
    ]