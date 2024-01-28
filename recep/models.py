from django.db import models
from django.contrib.auth.models import User
from tablero.models import Habitacion

from .choices import *

# MODELO PARA LA CREACION DE LAS RESERVAS

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=50)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    correo = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} {1}, Cedula{2}"
        return txt.format(self.nombre, self.apellido, self.cedula)


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    fechaEntrada = models.DateTimeField(auto_now_add=True, verbose_name="CheckIn")
    fechaSalida = models.DateTimeField(null=True, blank=True, verbose_name="CheckOut")
    estadoReserva = models.CharField(max_length=50, choices=estados, default="Pagada")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    importe = models.FloatField(max_length=50)
    metodoPago = models.CharField(max_length=100, choices=metodoPago, default="Divisas")
    moneda = models.CharField(max_length=100, choices=monedas, default="Dolares")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def detallesReserva(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.factura, self.fechaEntrada, self.fechaSalida, self.estadoReserva, self.user, self.habitacion, self.importe, self.metodoPago, self.moneda, self.cliente)

    def __str__(self):
        return self.detallesReserva()


