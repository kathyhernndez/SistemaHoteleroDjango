from django.db import models
from .choices import tipos, estados
from recep.choices import monedas

class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(unique=True, verbose_name="Numero de Habitacion: No pueden repetirse los numeros de habitaciones ya creadas.")
    estado = models.CharField(choices=estados, default="Disponible", verbose_name="Selecciona el estado por defecto que tendra la habitacion")
    precio = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Precio de la Habitacion")
    moneda = models.CharField(choices=monedas, default="Dolares", verbose_name="Selecciona la moneda utilizada para el precio de la habitacion")
    tipo = models.CharField(choices=tipos, default="Individual", verbose_name="Selecciona el tipo de Habitacion")
    


    def __str__(self):
        txt = "Tipo: {0}, Numero: {1}, Estado: {2}, Precio: {3}"
        return txt.format( self.tipo, self.numero, self.estado, self.precio, self.moneda)

    class Meta:
        db_table = 'Habitacion'
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'