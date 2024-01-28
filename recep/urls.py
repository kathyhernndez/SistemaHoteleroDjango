from django.urls import path
from . import views
from .views import homeReserva, registrarReserva, eliminarReserva, editarReserva

urlpatterns = [
    ## URLS DE PANEL DE RESERVAS
    path('homeReserva/', views.homeReserva, name='homeReserva'),

    #URL CRUD ACTUALIZAR, LEER, CREAR ELIMINAR,
    path('registrarReserva/', views.registrarReserva, name='registrarReserva'),
    path('eliminarReserva/<int:id>', views.eliminarReserva, name='eliminarReserva'),
    path('editarReserva/<int:pk>', views.editarReserva, name='editarReserva'),
    
   
]
