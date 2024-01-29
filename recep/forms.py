from django import forms
from .choices import *
from recep.models import *

class ReservaForm(forms.Form):
   habitacion = forms.ModelChoiceField(label="Habitacion", queryset=Habitacion.objects.all(), required=True)
   importe = forms.FloatField(label="Importe de Pago", required=True, min_value=0.5)
   monedas = forms.ChoiceField(choices = monedas, help_text=("Ingresa el metodo de pago y la moneda utilizada, para el mismo."))
   metodoPago = forms.ChoiceField(choices = metodoPago)
   cliente = forms.ModelChoiceField(label="Cliente", queryset=Cliente.objects.all(), required=True, help_text=("Si un cliente no se encuentra registrado, haz click en el boton Registrar Cliente, para registrarlo."))
   user = forms.ModelChoiceField(label="Usuario", queryset=User.objects.all(), required=True)

class ClienteForm(forms.Form):
   cedula = forms.CharField(label="Cedula", required=True)
   nombre = forms.CharField(label="Nombre y Apellido", required=True, help_text=("Los datos como nombre, apellido y cedula son necesarios para indentificar a los clientes."))
   apellido = forms.CharField(required=True)
   telefono = forms.CharField(label="Telefono", required=True)
   correo = forms.CharField(label="", required=True,
   help_text=("Ingresa el correo del cliente para recuperacion de usuario."))
