# Generated by Django 5.0.1 on 2024-01-29 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tablero', '0009_rename_id_tipohabitacion_habitacion_tipohabitacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habitacion',
            name='tipoHabitacion',
        ),
        migrations.AddField(
            model_name='habitacion',
            name='precio',
            field=models.FloatField(default=float, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='habitacion',
            name='tipo',
            field=models.CharField(choices=[('Doble Individual', 'Doble Individual'), ('Triple Individual', 'Triple Individual'), ('Matrimonial + Individual', 'Matrimonial + Individual'), ('Doble Matrimonial', 'Doble Matrimonial'), ('Matrimonial Queen', 'Matrimonial Queen'), ('Matrimonial King', 'Matrimonial King'), ('Matrimonial', 'Matrimonial')], default='Doble Individual', max_length=50),
        ),
        migrations.DeleteModel(
            name='TipoHabitacion',
        ),
    ]
