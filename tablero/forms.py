from django import forms
from .choices import *
from tablero.models import *

class HabitacionForm(forms.Form):
   id_tipoHabitacion = forms.ModelChoiceField(label="Tipo de Habitacion", queryset=TipoHabitacion.objects.all(), required=True)
   numero = forms.IntegerField(label="Numero de Habitacion", required=True)
   estado = forms.ChoiceField(choices = estados, required=True)
