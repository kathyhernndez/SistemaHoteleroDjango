from django.urls import path
from . import views
from .views import homeReserva, registrarReserva, editarReserva, eliminarReserva, registrarCliente, liberarReserva

urlpatterns = [
    ## URLS DE PANEL DE RESERVAS
    path('homeReserva/', views.homeReserva, name='homeReserva'),

    #URL CRUD ACTUALIZAR, LEER, CREAR ELIMINAR,
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),
    path('registrarReserva/<int:pk>', views.registrarReserva, name='registrarReserva'),
    path('liberarReserva/<int:id>', views.liberarReserva, name='liberarReserva'),
    path('editarReserva/<int:pk>', views.editarReserva, name='editarReserva'),
    path('eliminarReserva/<int:id>', views.eliminarReserva, name='eliminarReserva'),

]
