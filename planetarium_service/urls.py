from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Planetarium API. Visit /api/docs/ for documentation.")

urlpatterns = [
    path("", home),  # головна сторінка
    path("admin/", admin.site.urls),
    path("api/", include("planetarium.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]
