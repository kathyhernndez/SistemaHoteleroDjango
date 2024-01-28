from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required
from django.template import Context
from .models import Reserva
from api.views import ReservaViewSet
from .forms import reservaForm


# Create your views here.

@login_required
def homeReserva(request):
    response = requests.get('http://127.0.0.1:8000/api/reservas/')
    responseList = response.json()
    reservaList = responseList
    contexto  = {"reservaList": reservaList}
    
    return render(request,"reservas.html", contexto)

@login_required
def registrarReserva(request):
    if request.method == "GET":
        return render(request, 'formReserva.html', {"form": reservaForm})
    else:
        try:
            form = reservaForm(request.POST)
            nueva_reserva = form.save(commit=False)
            nueva_reserva.user = request.user
            nueva_reserva.save()
            return redirect('homeReserva')
        except ValueError:
            return render(request, 'formReserva.html', {"form": reservaForm, "error": "Error Creando Reserva."})
    

def eliminarReserva(request, code):
    reserva = Reserva.objects.get(code=code)
    reserva.delete()
    return redirect('homeReserva')


def editarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    data = {
        'titulo': 'Edicion de reservas',
        'reserva' : reserva
    }
    return render(request,'editarReserva.html', data)

def nuevaReserva(request):
    monto = request.POST['numMonto']
    pago = request.POST['textPago']
    cliente = request.POST['textCliente']
    cedula = request.POST['numCedula']
    contacto = request.POST['numContacto']

    reserva = Reserva.objects.get(id=id)
    reserva.monto = monto
    reserva.pago = pago
    reserva.cliente = cliente
    reserva.cedula = cedula
    reserva.contacto = contacto
    reserva.save()

    return redirect('homeReserva')





