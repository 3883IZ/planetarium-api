from rest_framework import serializers
from .models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = "__all__"


class AstronomyShowSerializer(serializers.ModelSerializer):
    # ✅ тепер можна передавати список ID тем при створенні/оновленні
    themes = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=ShowTheme.objects.all()
    )

    class Meta:
        model = AstronomyShow
        fields = "__all__"


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = "__all__"


class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show = AstronomyShowSerializer(read_only=True)
    planetarium_dome = PlanetariumDomeSerializer(read_only=True)

    astronomy_show_id = serializers.PrimaryKeyRelatedField(
        queryset=AstronomyShow.objects.all(),
        source="astronomy_show",
        write_only=True,
    )
    planetarium_dome_id = serializers.PrimaryKeyRelatedField(
        queryset=PlanetariumDome.objects.all(),
        source="planetarium_dome",
        write_only=True,
    )

    show_time = serializers.DateTimeField()

    class Meta:
        model = ShowSession
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
