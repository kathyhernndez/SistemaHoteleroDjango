from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .choices import *
from tablero.models import *


from django.forms import ModelForm

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['numero', 'estado', 'precio', 'moneda', 'tipo' ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))
   

