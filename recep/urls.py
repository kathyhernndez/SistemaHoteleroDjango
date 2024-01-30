from django.urls import path
from . import views
from .views import homeReserva, registrarReserva, editarReserva, eliminarReserva, registrarCliente, CheckoutView

urlpatterns = [
    ## URLS DE PANEL DE RESERVAS
    path('homeReserva/', views.homeReserva, name='homeReserva'),

    #URL CRUD ACTUALIZAR, LEER, CREAR ELIMINAR,
    path('registrarCliente/', views.registrarCliente, name='registrarCliente'),
    path('registrarReserva/<int:pk>', views.registrarReserva, name='registrarReserva'),
    path('CheckoutView/<int:pk>', views.CheckoutView, name='CheckoutView'),
    path('editarReserva/<int:pk>', views.editarReserva, name='editarReserva'),
    path('eliminarReserva/<int:id>', views.eliminarReserva, name='eliminarReserva'),

]
