from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
import requests
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.template import Context
from .models import Reserva, Cliente
from tablero.models import Habitacion
from api.views import ReservaViewSet
from .forms import ReservaForm, ClienteForm


# Create your views here.

@login_required
def homeReserva(request):
    reserva = Reserva.objects.all()
    
    contexto  = {"reserva": reserva}
    
    return render(request,"reservas.html", contexto)



@login_required
def registrarReserva(request, pk):

    form = ReservaForm()

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homeReserva')
    else:
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
            return redirect('homeReserva')
            
        else:
            print("Invalido")
        
    return render(request, 'formReserva.html', {'form': form})

@login_required
def eliminarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    reserva.delete()
    return redirect('appTablero')

@login_required
class CheckoutView(UpdateView):
    model = Reserva
    fields = ['fechaSalida']
    template_name_suffix = '_checkout_form'
    success_url = reverse_lazy('homeReserva')

    def form_valid(self, form):
        reserva = form.save(commit=False)
        reserva.habitacion.estado = 'Disponible'
        reserva.habitacion.save()
        reserva.save()
        return super().form_valid(form)



@login_required
def registrarCliente(request):
    form = ClienteForm()

    if request.method == "POST":

        print(request.POST)
        form = ClienteForm(request.POST) 

        if form.is_valid():
            print("Valido")
            
            cliente = Cliente()

            cliente.cedula = form.cleaned_data['cedula']
            cliente.nombre = form.cleaned_data['nombre']
            cliente.apellido = form.cleaned_data['apellido']
            cliente.telefono = form.cleaned_data['telefono']

            cliente.save()
            return redirect('registrarReserva')
    
        else:
            print("Invalido")

    return render(request, 'clienteForms.html', {'form': form})