from django.urls import path
from . import views
from .views import appTablero, formHabitacion, registrarHabitacion, eliminarHabitacion, editarHabitacion, nuevaHabitacion

urlpatterns = [
    path('appTablero/', views.appTablero, name='appTablero'),
    path('formHabitacion', views.formHabitacion),
    path('registrarHabitacion', views.registrarHabitacion, name='registrarHabitacion'),
    path('eliminarHabitacion/<int:numero>', views.eliminarHabitacion, name='eliminarHabitacion'),
    path('editarHabitacion/<int:numero>', views.editarHabitacion, name='editarHabitacion'),
    path('nuevaHabitacion/', views.nuevaHabitacion, name='nuevaHabitacion'),
]
