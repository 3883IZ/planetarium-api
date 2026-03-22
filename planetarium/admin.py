from django.contrib import admin
from planetarium.models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)


@admin.register(ShowTheme)
class ShowThemeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(AstronomyShow)
class AstronomyShowAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    search_fields = ("title",)
    list_filter = ("themes",)


@admin.register(PlanetariumDome)
class PlanetariumDomeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "rows", "seats_in_row")
    search_fields = ("name",)


@admin.register(ShowSession)
class ShowSessionAdmin(admin.ModelAdmin):
    list_display = ("id", "astronomy_show", "planetarium_dome", "show_time")
    list_filter = ("planetarium_dome", "show_time")
    search_fields = ("astronomy_show__title",)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username",)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "show_session", "reservation", "row", "seat")
    list_filter = ("show_session", "row")
    search_fields = ("reservation__user__username",)
