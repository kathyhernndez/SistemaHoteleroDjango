# Generated by Django 5.0.1 on 2024-01-27 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0002_alter_habitacion_estado_alter_tipohabitacion_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipohabitacion',
            name='descripcion',
            field=models.CharField(max_length=2000),
        ),
    ]