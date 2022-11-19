from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from swapi.views import PlanetViewSet, PeopleViewSet

router = routers.DefaultRouter()
router.register(r"planet", PlanetViewSet, basename="Planet")
router.register(r"people", PeopleViewSet, basename="People")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
