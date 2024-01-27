from django.urls import path
from . import views
from .views import appTablero, formHabitacion, registrarHabitacion, eliminarHabitacion, editarHabitacion, nuevaHabitacion

urlpatterns = [
    ## URLS DE PANEL DE HABITACIONES
    path('appTablero/', views.appTablero, name='appTablero'),

     #URL CRUD ACTUALIZAR, LEER, CREAR ELIMINAR,
    path('formHabitacion', views.formHabitacion),
    path('registrarHabitacion/', views.registrarHabitacion, name='registrarHabitacion'),
    path('eliminarHabitacion/<int:id>', views.eliminarHabitacion, name='eliminarHabitacion'),
    path('editarHabitacion/<int:id>', views.editarHabitacion, name='editarHabitacion'),
    path('nuevaHabitacion/', views.nuevaHabitacion, name='nuevaHabitacion'),
]
