from django.db import models

from .choices import tipos

class tipoHabitacion(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=30, choices=tipos, default="Disponible")
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField(max_length=50)

    def detallesHabitacion(self):
        return "{}, {}, {}".format(self.tipo, self.descripcion, self.precio)

    def __str__(self):
        return self.detallesHabitacion()
    
    class Meta:
        db_table = 'tipoHabitacion'
        verbose_name = 'Tipo de Habitacion'
        verbose_name_plural = 'Tipos de Habitaciones'

class Habitacion(models.Model):
    id = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    estado = models.CharField(max_length=50)
    id_tipoHabitacion = models.ForeignKey(tipoHabitacion, null=True, blank=True, verbose_name="Tipo de Habitacion", on_delete=models.CASCADE)

    def __str__(self):
        txt = "Habitacion {0}, Numero: {1}, Estado: {2}"
        return txt.format( self.id_tipoHabitacion, self.numero, self.estado)

    class Meta:
        db_table = 'Habitacion'
        verbose_name = 'Habitacion'
        verbose_name_plural = 'Habitaciones'