from django.urls import path
from . import views
from .views import homeReserva, registrarReserva, eliminarReserva, editarReserva, registrarCliente

urlpatterns = [
    ## URLS DE PANEL DE RESERVAS
    path('homeReserva/', views.homeReserva, name='homeReserva'),

    #URL CRUD ACTUALIZAR, LEER, CREAR ELIMINAR,
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),
    path('registrarReserva/<int:pk>', views.registrarReserva, name='registrarReserva'),
    path('eliminarReserva/<int:pk>', views.eliminarReserva, name='eliminarReserva'),
    path('editarReserva/<int:pk>', views.editarReserva, name='editarReserva'),
]
