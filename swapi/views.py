import requests
from django_filters.rest_framework import DjangoFilterBackend
from requests.api import get
from rest_framework import filters, generics, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from swapi import Atualizar
from swapi.models import People, Planet
from swapi.serializers import PeopleSerializer, PlanetSerializer


class PlanetViewSet(generics.ListCreateAPIView):
    """Lists all the plantes from SWAPI"""

    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer

    def get(self, request):

        Atualizar.Atualiza_Planets("https://swapi.dev/api/planets/")
        queryset = self.get_queryset()
        serializer = PlanetSerializer(queryset, many=True)
        try:
            results = requests.get("https://swapi.dev/api/planets/")
            results = results.json()
            return Response(results)
        except:
            return Response(serializer.data)


class SearchPlanet(APIView):
    # queryset = Planet.objects.filter()
    # serializer_class = PlanetSerializer
    def get(self, request, name, format=None):

        # Fetch SWAPI JSON data.
        Atualizar.Atualiza_Planets("https://swapi.dev/api/planets/?search={}".format(name))
        # queryset = self.get_queryset()
        # serializer = PlanetSerializer(queryset, many=True)
        results = requests.get("https://swapi.dev/api/planets/?search={}".format(name))
        results = results.json()

        return Response(results)


class SearchPeople(APIView):
    def get(self, request, name, format=None):

        Atualizar.Atualiza_Peoples("https://swapi.dev/api/people/?search={}".format(name))
        results = requests.get("https://swapi.dev/api/people/?search={}".format(name))
        results = results.json()
        return Response(results)


class PeopleViewSet(generics.ListCreateAPIView):
    """Lists all the people from SWAPI"""

    queryset = People.objects.all()
    serializer_class = PeopleSerializer

    def get(self, request):
        Atualizar.Atualiza_Peoples("https://swapi.dev/api/people/")
        queryset = self.get_queryset()
        serializer = PeopleSerializer(queryset, many=True)
        try:
            results = requests.get("https://swapi.dev/api/people/")
            results = results.json()
            return Response(results)
        except:
            return Response(serializer.data)


class ApiHome(APIView):
    def get(self, request, format=None):
        return Response(
            {
                "people": reverse("peoples-list", request=request, format=format),
                "planets": reverse("planets-list", request=request, format=format),
            }
        )
