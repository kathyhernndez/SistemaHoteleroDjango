from django.shortcuts import render, redirect
import requests
from django.contrib.auth.decorators import login_required
from django.template import Context
from .models import Reserva
from api.views import ReservaViewSet
from .forms import ReservaForm


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
    form = ReservaForm()

    if request.method == "POST":
        print(request.POST)
    

    return render(request, 'formReserva.html', {'form': form})
    
@login_required
def eliminarReserva(request, code):
    reserva = Reserva.objects.get(code=code)
    reserva.delete()
    return redirect('homeReserva')

@login_required
def editarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    data = {
        'titulo': 'Edicion de reservas',
        'reserva' : reserva
    }
    return render(request,'editarReserva.html', data)
    
@login_required
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





