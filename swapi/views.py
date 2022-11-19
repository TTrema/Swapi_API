from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from swapi import Atualizar
from swapi.models import People, Planet
from swapi.serializers import PeopleSerializer, PlanetSerializer


class PlanetViewSet(viewsets.ModelViewSet):
    """Listando clientes"""

    queryset = Planet.objects.all()
    serializer_class = PlanetSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["name"]
    search_fields = ["name"]

    @action(detail=False, methods=["GET"])
    def Atualizar_Dados(self, *args, **options):
        Planet.objects.all().delete()
        Atualizar.Atualiza_Planets("https://swapi.dev/api/planets/")
        return Response("Atualizado")

    # @action(detail=False, methods=["GET"])
    # def deletar_tudo(self, *args, **options):
    #     Planet.objects.all().delete()
    #     return Response("Banco de dados deletado")


class PeopleViewSet(viewsets.ModelViewSet):
    """Listando clientes"""

    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ["name"]
    search_fields = ["name"]

    @action(detail=False, methods=["GET"])
    def Atualizar_Dados(self, *args, **options):
        People.objects.all().delete()
        Atualizar.Atualiza_Peoples("https://swapi.dev/api/people/")
        return Response("Atualizado")

    # @action(detail=False, methods=["GET"])
    # def deletar_tudo(self, *args, **options):
    #     People.objects.all().delete()
    #     return Response("Banco de dados deletado")
