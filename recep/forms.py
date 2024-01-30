from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .choices import *
from recep.models import *

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['habitacion', 'cliente', 'importe', 'metodoPago', 'moneda', 'tiempoEstadia']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Guardar'))



class ClienteForm(forms.Form):
   cedula = forms.CharField(label="Cedula", required=True)
   nombre = forms.CharField(label="Nombre y Apellido", required=True, help_text=("Los datos como nombre, apellido y cedula son necesarios para indentificar a los clientes."))
   apellido = forms.CharField(required=True)
   telefono = forms.CharField(label="Telefono", required=True)
   
