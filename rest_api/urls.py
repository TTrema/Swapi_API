from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from swapi.views import PlanetViewSet, PeopleViewSet, ApiHome, SearchPlanet, SearchPeople


urlpatterns = format_suffix_patterns(
    [
        path("admin/", admin.site.urls),
        path("", ApiHome.as_view(), name="api-root"),
        path("planets/", PlanetViewSet.as_view(), name="planets-list"),
        re_path("planets/search/(?P<name>[\w\d-]+)/", SearchPlanet.as_view(), name="search-planet"),
        path("people/", PeopleViewSet.as_view(), name="peoples-list"),
        re_path("people/search/(?P<name>[\w\d-]+)/", SearchPeople.as_view(), name="search-people"),
    ]
)
