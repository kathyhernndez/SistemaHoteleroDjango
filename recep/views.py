from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
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
        form = ReservaForm(request.POST) 

        if form.is_valid():
            print("Valido")
            
            reserva = Reserva()

            reserva.habitacion = form.cleaned_data['habitacion']
            reserva.importe = form.cleaned_data['importe']
            reserva.monedas = form.cleaned_data['monedas']
            reserva.metodoPago = form.cleaned_data['metodoPago']
            reserva.cliente = form.cleaned_data['cliente']
            reserva.user = form.cleaned_data['user']

            reserva.save()

            return redirect('homeReserva')
    
        else:
            print("Invalido")

    return render(request, 'formReserva.html', {'form': form})




@login_required
def editarReserva(request, pk):
    
    reserva = get_object_or_404(Reserva, id=pk)

    form = ReservaForm(initial={'habitacion': reserva.habitacion, 'importe': reserva.importe, 'monedas': reserva.moneda, 'metodoPago': reserva.metodoPago, 'cliente': reserva.cliente, 'user': reserva.user})

    if request.method == "POST":
        print(request.POST)
        form = ReservaForm(request.POST) 

        if form.is_valid():
            print("Valido")

            reserva.habitacion = form.cleaned_data['habitacion']
            reserva.importe = form.cleaned_data['importe']
            reserva.monedas = form.cleaned_data['monedas']
            reserva.metodoPago = form.cleaned_data['metodoPago']
            reserva.cliente = form.cleaned_data['cliente']
            reserva.user = form.cleaned_data['user']

            reserva.save()

            return redirect('homeReserva')
    
        else:
            print("Invalido")
        
    return render(request, 'formReserva.html', {'form': form})



@login_required
def eliminarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('homeReserva')

