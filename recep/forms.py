from django.forms import ModelForm
from .models import Reserva

class reservaForm(ModelForm):
    class Meta:
        model = Reserva
        fields = ['monto', 'pago', 'cliente', 'cedula', 'contacto']