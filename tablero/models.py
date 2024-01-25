from django.db import models

class Habitacion(models.Model):
    numero = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

    def __str__(self):
        txt = "Habitacion {0}"
        return txt.format( self.tipo)