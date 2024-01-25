from rest_framework.routers import DefaultRouter
from api.views import ReservaViewSet, HabitacionViewSet


router = DefaultRouter()
router.register('reservas', ReservaViewSet, basename='reserva')
router.register('habitaciones', HabitacionViewSet, basename='habitacion')

urlpatterns = router.urls
