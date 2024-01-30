from django.db import models

from .choices import tipos, estados

class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField(unique=True)
    estado = models.CharField(max_length=50, choices=estados, default="Disponible")
    precio = models.FloatField(max_length=10)
    tipo = models.CharField(max_length=50, choices=tipos, default="Doble Individual")


    def __str__(self):
        txt = "Tipo: {0}, Numero: {1}, Estado: {2}, Precio: {3}"
        return txt.format( self.tipo, self.numero, self.estado, self.precio)

    class Meta:
        db_table = 'Habitacion'
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'