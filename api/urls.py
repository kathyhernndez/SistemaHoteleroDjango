from rest_framework.routers import DefaultRouter
from api.views import ReservaViewSet, HabitacionViewSet, ClienteViewSet, IngresoViewSet, MetodoPagoViewSet, TipoHabitacionViewSet


router = DefaultRouter()
router.register('reservas', ReservaViewSet, basename='reserva')
router.register('habitaciones', HabitacionViewSet, basename='habitacion')
router.register('clientes', ClienteViewSet, basename='cliente')
router.register('ingresos', IngresoViewSet, basename='ingreso')
router.register('metodosPagos', MetodoPagoViewSet, basename='metodoPago')
router.register('tiposhabitaciones', TipoHabitacionViewSet, basename='tipoHabitacion')

urlpatterns = router.urls
