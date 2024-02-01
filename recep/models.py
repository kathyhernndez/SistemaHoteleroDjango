from django.db import models
from django.contrib.auth.models import User
from tablero.models import Habitacion
from django.utils import timezone

from .choices import *

# MODELO PARA LA CREACION DE LAS RESERVAS

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(max_length=9, unique=True, verbose_name="Ingresa la Cedula del Cliente")
    nombre = models.CharField(max_length=15, verbose_name="Escribe el nombre del Cliente")
    apellido = models.CharField(max_length=15, verbose_name="Escribe el apellido del Cliente")
    telefono = models.CharField(max_length=12, verbose_name="Ingresa el numero telefonico del Cliente")
    correo = models.EmailField(max_length=50, verbose_name="Inngresa el correo del Cliente")

    def __str__(self):
        txt = "{0} {1}, Cedula: V-{2}"
        return txt.format(self.nombre, self.apellido, self.cedula)


class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    fechaEntrada = models.DateTimeField(auto_now_add=True, verbose_name="CheckIn")
    fechaSalida = models.DateTimeField(null=True, blank=True, verbose_name="CheckOut")
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, verbose_name="Selecciona la habitacion",)
    importe = models.DecimalField(max_digits=6, decimal_places=2, null=True, verbose_name="Importe de Pago de la Reserva")
    metodoPago = models.CharField(choices=metodoPago, default="Divisas", verbose_name="Metodo de Pago Utilizado",)
    moneda = models.CharField(choices=monedas, default="Dolares", verbose_name="Moneda Utilizada para el pago de la Reserva")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Selecciona el cliente. Si el cliente no encuentra registrado, haz click en registrar cliente, para registrar uno nuevo.")

    def detallesReserva(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self.fechaEntrada, self.fechaSalida,  self.habitacion, self.importe, self.metodoPago, self.moneda, self.cliente)

    def __str__(self):
        return self.detallesReserva()
    
    def save(self, *args, **kwargs):
        # Actualiza el estado de la habitación a "ocupado"
        self.habitacion.estado = 'Ocupado'
        self.habitacion.save()
        super().save(*args, **kwargs)

#Checkout
    def liberarReserva(self, *args, **kwargs):
        self.fechaSalida = timezone.now()
        self.save()

    def liberar(self, *args, **kwargs):
        # Actualiza el estado de la habitación a "ocupado"
        self.habitacion.estado = 'Disponible'
        self.habitacion.save()
        super().save(*args, **kwargs)

