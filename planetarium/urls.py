from rest_framework.routers import DefaultRouter
from planetarium.views import (
    ShowThemeViewSet,
    AstronomyShowViewSet,
    PlanetariumDomeViewSet,
    ShowSessionViewSet,
    ReservationViewSet,
    TicketViewSet,
)

router = DefaultRouter()
router.register(r"themes", ShowThemeViewSet)
router.register(r"shows", AstronomyShowViewSet)
router.register(r"domes", PlanetariumDomeViewSet)
router.register(r"sessions", ShowSessionViewSet)
router.register(r"reservations", ReservationViewSet)
router.register(r"tickets", TicketViewSet)

urlpatterns = router.urls
