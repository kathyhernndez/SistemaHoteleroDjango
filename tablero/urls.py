from django.urls import path
from .views import appTablero, formHabitacion, registrarHabitacion, eliminarHabitacion, editarHabitacion, nuevaHabitacion

urlpatterns = [
    path('appTablero', appTablero),
    path('formHabitacion', formHabitacion),
    path('registrarHabitacion', registrarHabitacion),
    path('eliminarHabitacion/<int:numero>', eliminarHabitacion, name='eliminarHabitacion'),
    path('editarHabitacion/<int:numero>', editarHabitacion, name='editarHabitacion'),
    path('nuevaHabitacion/', nuevaHabitacion, name='nuevaHabitacion'),
]
