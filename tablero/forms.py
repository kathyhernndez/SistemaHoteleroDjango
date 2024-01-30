from django import forms
from .choices import *
from tablero.models import *


from django.forms import ModelForm

class HabitacionForm(forms.Form):
   numero = forms.IntegerField(label="Numero de Habitacion")
   estado = forms.ChoiceField( choices = estados)
   precio = models.FloatField(max_length=10)
   tipo = models.CharField(choices=tipos, default="Doble Individual")

