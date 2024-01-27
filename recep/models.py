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
        txt = "{0} {1}, Cedula{2}, Telefono: {3}, Correo: {4}"
        return txt.format(self.nombre, self.apellido, self.cedula, self.telefono, self.correo)

class MetodoPago(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=100, choices=tipos, default="Divisas")
    moneda = models.CharField(max_length=100, choices=monedas, default="Dolares")

    def __str__(self):
        txt = "{0} {1}"
        return txt.format(self.tipo, self.moneda)

    class Meta:
        db_table = 'MetodoPago'
        verbose_name = 'Metodo de Pago'
        verbose_name_plural = 'Metodos de Pagos'

class Ingreso(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now_add=True)
    importe = models.FloatField(max_length=50)
    id_metodoPago = models.ForeignKey(MetodoPago, null=True, blank=True, verbose_name="Metodo de Pago", on_delete=models.CASCADE)

    def __str__(self):
        txt = "Fecha {0}, Importe {1}, Detalles del Pago {2}"
        return txt.format( self.fecha, self.importe, self.id_metodoPago)

    class Meta:
        db_table = 'Ingreso'
        verbose_name = 'Ingreso'
        verbose_name_plural = 'Ingresos'

class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    factura = models.CharField()
    fechaEntrada = models.DateTimeField(auto_now_add=True, verbose_name="CheckIn")
    fechaSalida = models.DateTimeField(null=True, blank=True, verbose_name="CheckOut")
    estadoReserva = models.CharField(max_length=50, choices=estados, default="Pagada")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    importe = models.ForeignKey(Ingreso, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def detallesReserva(self):
        return "{}, {}, {}, {}, {}, {}, {}, {}".format(self.factura, self.fechaEntrada, self.fechaSalida, self.estadoReserva, self.user, self.habitacion, self.importe, self.cliente)

    def __str__(self):
        return self.detallesReserva()


