from django.db import models
from django.contrib.auth.models import User
from tablero.models import Habitacion


# MODELO PARA LA CREACION DE LAS RESERVAS

class Reserva(models.Model):
    code = models.AutoField(primary_key=True)
    monto = models.PositiveSmallIntegerField(default=30, blank=False)
    pago = models.CharField(max_length=20)
    fechaEntrada = models.DateTimeField(auto_now_add=True, verbose_name="CheckIn")
    cliente = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    contacto = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE)

    def __str__(self):
        txt = "Pago {0} por {1}, Cliente: {2}, Cedula: {3}, Telefono: {4}, CheckIn: {5}"
        return txt.format(self.monto, self.pago, self.cliente, self.cedula, self.contacto, self.fechaEntrada)

