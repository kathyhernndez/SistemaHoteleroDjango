from django import forms
from .choices import *
from recep.models import *

class ReservaForm(forms.Form):
   habitacion = forms.ModelChoiceField(label="Habitacion", queryset=Habitacion.objects.all(), required=True)
   importe = forms.FloatField(label="Importe de Pago", required=True, min_value=0.5)
   monedas = forms.ChoiceField(choices = monedas, help_text=("Ingresa el metodo de pago y la moneda utilizada, para el mismo."))
   metodoPago = forms.ChoiceField(choices = metodoPago)
   cliente = forms.CharField(label='Cedula', max_length=9)


class ClienteForm(forms.Form):
   cedula = forms.CharField(label="Cedula", required=True)
   nombre = forms.CharField(label="Nombre y Apellido", required=True, help_text=("Los datos como nombre, apellido y cedula son necesarios para indentificar a los clientes."))
   apellido = forms.CharField(required=True)
   telefono = forms.CharField(label="Telefono", required=True)
