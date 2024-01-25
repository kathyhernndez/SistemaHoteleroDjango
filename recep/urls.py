from django.urls import path
from .views import homeReserva, registrarReserva, eliminarReserva, editarReserva, nuevaReserva, home

urlpatterns = [
    path('homeReserva', homeReserva, name='homeReserva'),
    path('registrarReserva', registrarReserva),
    path('eliminarReserva/<int:code>', eliminarReserva, name='eliminarReserva'),
    path('editarReserva/<int:code>', editarReserva, name='editarReserva'),
    path('nuevaReserva/', nuevaReserva),
    
]
