from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
import requests
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.template import Context
from .models import Reserva, Cliente
from tablero.models import Habitacion
from api.views import ReservaViewSet
from .forms import ReservaForm, ClienteForm
import datetime
import pytz

utc_time = datetime.datetime.now(pytz.utc)


# Create your views here.

@login_required
def homeReserva(request):
    reserva = Reserva.objects.all()
    
    contexto  = {"reserva": reserva}
    
    return render(request,"reservas.html", contexto)



@login_required
def registrarReserva(request):

    form = ReservaForm()

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'La Reserva ha sido creada.')
            return redirect('homeReserva')
        else:
            messages.success(request, 'Los datos son incorrectos.')
    form = ReservaForm(initial={'habitacion': request.GET.get('habitacion.id')})
    return render(request, 'formReserva.html', {'form': form})




@login_required
def editarReserva(request, pk):
    
    reserva = get_object_or_404(Reserva, id=pk)

    form = ReservaForm(initial={'habitacion': reserva.habitacion, 'importe': reserva.importe, 'monedas': reserva.moneda, 'metodoPago': reserva.metodoPago, 'cliente': reserva.cliente})

    if request.method == "POST":
        print(request.POST)
        form = ReservaForm(request.POST) 

        if form.is_valid():
            print("Valido")

            reserva.habitacion = form.cleaned_data['habitacion']
            reserva.importe = form.cleaned_data['importe']
            reserva.moneda = form.cleaned_data['moneda']
            reserva.metodoPago = form.cleaned_data['metodoPago']
            reserva.cliente = form.cleaned_data['cliente']
            reserva.tiempoEstadia = form.cleaned_data['tiempoEstadia']
            

            reserva.save()
            messages.success(request, 'La Reserva ha sido actualizada')
            return redirect('homeReserva')
            
        else:
            print("Invalido")
        
    return render(request, 'formReserva.html', {'form': form})

@login_required
def eliminarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    if request.method == 'POST':
        reserva.delete()
        messages.success(request, 'La Reserva ha sido eliminada.')
        return redirect('homeReserva')
    context = {'reserva': reserva}
    return render(request, 'eliminarReserva.html', context)


@login_required
def liberarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    if request.method == 'POST':
        reserva.liberarReserva()
        reserva.liberar()
        messages.success(request, 'La Reserva ha sido liberada.')
        return redirect('homeReserva')
    context = {'reserva': reserva}
    return render(request, 'confirmarCheck.html', context)




@login_required
def registrarCliente(request):

    form = ClienteForm()

    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registrarReserva')
    return render(request, 'clienteForms.html', {'form': form})