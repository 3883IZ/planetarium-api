from rest_framework import viewsets
from .models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)
from .serializers import (
    ShowThemeSerializer,
    AstronomyShowSerializer,
    PlanetariumDomeSerializer,
    ShowSessionSerializer,
    ReservationSerializer,
    TicketSerializer,
)


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()   # ✅ додали queryset
    serializer_class = AstronomyShowSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        theme = self.request.query_params.get("theme")
        if theme:
            queryset = queryset.filter(themes__name__icontains=theme)
        return queryset


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
