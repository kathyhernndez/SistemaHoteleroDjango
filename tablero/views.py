from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
import requests
import pymsgbox
from django.template import Context
from recep.models import Habitacion
from api.views import HabitacionViewSet
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.

@login_required
def appTablero(request):
    responseHab = requests.get('http://127.0.0.1:8000/api/habitaciones/')
    responseList = responseHab.json()
    habitacionList = responseList
    contexto  = {"habitacionList": habitacionList}
    
    return render(request,"tablero.html", contexto)


@login_required
def registrarHabitacion(request):
    form = HabitacionForm()
    if request.method == 'POST':
        form = HabitacionForm(request.POST)
        if form.is_valid():
            print("valido")
            form.save()
            messages.success(request, 'La Hbitacion ha sido creada.')
            return redirect('appTablero')
        else:
            print("Invalido")
    return render(request, 'formHabitacion.html', {'form': form})



@login_required
def eliminarHabitacion(request, id):
    habitacion = Habitacion.objects.get(id=id)
    if request.method == 'POST':
        habitacion.delete()
        messages.success(request, 'La Habitacion ha sido eliminada.')
        return redirect('appTablero')
    context = {'habitacion': habitacion}
    return render(request, 'eliminarHabitacion.html', context)

