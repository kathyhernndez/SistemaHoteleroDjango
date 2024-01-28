from django import forms
from .choices import *
from tablero.models import Habitacion
from recep.models import *

class ReservaForm(forms.Form):
   habitacion = forms.ModelChoiceField(label="Habitacion", queryset=Habitacion.objects.all(), required=True)
   importe = forms.FloatField(label="Importe de Pago", required=True, min_value=0.5)
   monedas = forms.ChoiceField(choices = monedas, required=True,)
   metodoPago = forms.ChoiceField(choices = metodoPago, required=True,)
   cliente = forms.ModelChoiceField(label="Cliente", queryset=Cliente.objects.all(), required=True)
   
