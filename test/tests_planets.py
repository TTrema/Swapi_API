from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from swapi.models import Planet


class CursosTestCase(APITestCase):
    def setUp(self):
        self.data = Planet.objects.all()
        self.list_url = reverse("planets-list")
        self.url = reverse("search-planet", args=["da"])
        self.planet = Planet.objects.create(
            name="Skako",
            terrain="xxxx",
        )

    def test_get(self):
        """Test para verificar se está conseguindo listar e baixar a lista para o banco de dados"""
        conection = self.client.get(self.list_url)
        response = [i.name for i in self.data]
        self.assertEqual(conection.status_code, status.HTTP_200_OK)
        self.assertIn("Hoth", response)
        self.assertIn("Kashyyyk", response)
        self.assertIn("Rodia", response)
        self.assertIn("Malastare", response)
        self.assertIn("Muunilinst", response)

    def test_procura(self):
        """Teste para ver se a pesquisa retorna os valores corretos e salva no banco de dados"""
        conection = self.client.get(self.url)
        response = [i.name for i in self.data]
        self.assertEqual(conection.status_code, status.HTTP_200_OK)
        self.assertIn("Dagobah", response)
        self.assertIn("Dantooine", response)
        self.assertIn("Toydaria", response)
        self.assertIn("Dathomir", response)
        self.assertIn("Concord Dawn", response)

    def test_repetido(self):
        """Teste para ver se a pesquisa não adiciona e nem altera banco de dados quando já tem um nome igual"""
        self.client.get(reverse("search-people", args=["Skako"]))
        response = [i.terrain for i in self.data]
        self.assertEqual(len(self.data), 1)
        self.assertIn("xxxx", response)
