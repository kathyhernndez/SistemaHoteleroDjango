from django import forms
from .choices import *
from tablero.models import *

class HabitacionForm(forms.Form):
   id_tipoHabitacion = forms.ModelChoiceField(label="Tipo de Habitacion", queryset=TipoHabitacion.objects.all(), required=True)
   numero = forms.IntegerField(label="Numero de Habitacion", required=True)
   estado = forms.ChoiceField(choices = estados, required=True)

class TipoHabitacionForm(forms.Form):
   tipo = forms.ChoiceField(choices= tipos, required=True)
   precio = forms.FloatField(label="Precio de Habitacion", required=True)
   descripcion = forms.CharField(label="Descripcion de Habitacion", required=True)