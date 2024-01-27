from rest_framework.routers import DefaultRouter
from api.views import ReservaViewSet, HabitacionViewSet, ClienteViewSet, TipoHabitacionViewSet


router = DefaultRouter()
router.register('reservas', ReservaViewSet, basename='reserva')
router.register('habitaciones', HabitacionViewSet, basename='habitacion')
router.register('clientes', ClienteViewSet, basename='cliente')
router.register('tiposhabitaciones', TipoHabitacionViewSet, basename='tipoHabitacion')

urlpatterns = router.urls
