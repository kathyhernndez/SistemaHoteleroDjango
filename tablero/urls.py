from django.urls import path
from . import views
from .views import appTablero, registrarHabitacion, eliminarHabitacion, editarHabitacion

urlpatterns = [
    ## URLS DE PANEL DE HABITACIONES
    path('appTablero/', views.appTablero, name='appTablero'),

     #URL CRUD ACTUALIZAR, LEER, CREAR ELIMINAR,
    path('registrarHabitacion/', views.registrarHabitacion, name='registrarHabitacion'),
    path('eliminarHabitacion/<int:id>', views.eliminarHabitacion, name='eliminarHabitacion'),
    path('editarHabitacion/<int:pk>', views.editarHabitacion, name='editarHabitacion'),    
]

