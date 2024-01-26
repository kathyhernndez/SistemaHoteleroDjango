from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, FormView, View, DeleteView
from django.urls import reverse, reverse_lazy
import requests
import pymsgbox
from django.template import Context
from recep.models import Habitacion
from api.views import HabitacionViewSet
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def appTablero(request):
    responseHab = requests.get('http://127.0.0.1:8000/api/habitaciones/')
    responseList = responseHab.json()
    habitacionList = responseList
    contexto  = {"habitacionList": habitacionList}
    
    return render(request,"tablero.html", contexto)

def formHabitacion(request):
    pass
    return render(request, "formHabitacion.html")

def registrarHabitacion(request):
    tipo = request.POST['texTipo']
    estado = request.POST['textEstado']

    habitacion = Habitacion.objects.create(tipo=tipo, estado=estado)
    return redirect('appTablero')


def eliminarHabitacion(request, numero):
    habitacion = Habitacion.objects.get(numero=numero)
    habitacion.delete()
    return redirect('appTablero')

def editarHabitacion(request, numero):
    habitacion = Habitacion.objects.get(numero=numero)
    data = {
        'titulo': 'Edicion de Habitaciones',
        'habitacion' : habitacion
    }
    return render(request,"formEditar.html", data)

def nuevaHabitacion(request):
    numero = request.POST['numero']
    tipo = request.POST['texTipo']
    estado = request.POST['textEstado']

    habitacion = Habitacion.objects.get(numero=numero)
    habitacion.tipo = tipo
    habitacion.estado = estado
    habitacion.save()

    return redirect(appTablero)