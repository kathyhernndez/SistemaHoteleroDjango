from django.db import models

from .choices import tipos, estados

class TipoHabitacion(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, choices=tipos, default="Disponible")
    descripcion = models.CharField(max_length=2000)
    precio = models.FloatField(max_length=100)

    def detallesHabitacion(self):
        return "{}, {}, {}".format(self.tipo, self.descripcion, self.precio)

    def __str__(self):
        return self.detallesHabitacion()
    
    class Meta:
        db_table = 'TipoHabitacion'
        verbose_name = 'Tipo de Habitacion'
        verbose_name_plural = 'Tipos de Habitaciones'

class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    estado = models.CharField(max_length=50, choices=estados, default="Disponible")
    id_tipoHabitacion = models.ForeignKey(TipoHabitacion, null=True, blank=True, verbose_name="Tipo de Habitacion", on_delete=models.CASCADE)

    def __str__(self):
        txt = "Habitacion {0}, Numero: {1}, Estado: {2}"
        return txt.format( self.id_tipoHabitacion, self.numero, self.estado)

    class Meta:
        db_table = 'Habitacion'
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'