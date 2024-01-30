from rest_framework import serializers
from recep.models import Reserva, Cliente
from tablero.models import Habitacion

##### serializers de la app recep ############

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


##### serializers de la app tablero ############


class HabitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitacion
        fields = '__all__'

