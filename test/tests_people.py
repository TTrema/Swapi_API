from rest_framework.test import APITestCase
from swapi.models import People
from django.urls import reverse
from rest_framework import status


class PeopleTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("peoples-list")
        self.search_url = reverse("search-people")
        self.people = People.objects.create(
            name="Luke Skywalker",
            height="172",
            mass="77",
            hair_color="blond",
            skin_color="fair",
            eye_color="blue",
            birth_year="19BBY",
            gender="male",
            homeworld="https://swapi.dev/api/planets/1/",
        )

    def test_requisicao_get_para_listar_personagens(self):
        """Test para verificar a requisição GET para listar os personagens"""
        name = "luke"
        response = self.client.get(self.search_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_verifica_atributos_dos_personagens(self):
        """Teste que verifica os atributos estão sendo corretamente salvos e recuperados"""
        self.assertEqual(self.people.name, "Luke Skywalker")
        self.assertEqual(self.people.height, "172")
        self.assertEqual(self.people.mass, "77")
        self.assertEqual(self.people.hair_color, "blond")
        self.assertEqual(self.people.homeworld, "https://swapi.dev/api/planets/1/")

    # def test_para_não_poder_ter_nome_repetido(self):
    #     """Teste que verifica se não tem como inserir 2 nomes iguais no banco de dados"""
    #     self.people2 = People.objects.create(name="Luke Skywalker", height="172", mass="77", hair_color="blond",
    #     skin_color="fair", eye_color="blue", birth_year="19BBY", gender="male", homeworld="https://swapi.dev/api/planets/1/")
    #     self.assertRaises(FooException, self.people2)
