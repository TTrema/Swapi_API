from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from swapi.models import People


class PeopleTestCase(APITestCase):
    def setUp(self):
        self.data = People.objects.all()
        self.list_url = reverse("peoples-list")
        self.url = reverse("search-people", args=["da"])

        self.people = People.objects.create(
            name="Luke Skywalker",
            height="xxxx",
            mass="xxxx",
            hair_color="xxxx",
            skin_color="xxxx",
            eye_color="xxxx",
            birth_year="xxxx",
            gender="xxxx",
            homeworld="xxxx",
        )

    def test_get(self):
        """Test para verificar se está conseguindo listar e baixar a lista para o banco de dados"""
        conection = self.client.get(self.list_url)
        response = [i.name for i in self.data]
        self.assertEqual(conection.status_code, status.HTTP_200_OK)
        self.assertIn("Qui-Gon Jinn", response)
        self.assertIn("R5-D4", response)
        self.assertIn("Jek Tono Porkins", response)
        self.assertIn("Mas Amedda", response)
        self.assertIn("Tion Medon", response)

    def test_procura(self):
        """Teste para ver se a pesquisa retorna os valores corretos e salva no banco de dados"""
        conection = self.client.get(self.url)
        response = [i.name for i in self.data]
        self.assertEqual(conection.status_code, status.HTTP_200_OK)
        self.assertIn("Darth Vader", response)
        self.assertIn("Biggs Darklighter", response)
        self.assertIn("Yoda", response)
        self.assertIn("Padmé Amidala", response)
        self.assertIn("Mas Amedda", response)

    def test_repetido(self):
        """Teste para ver se a pesquisa não adiciona e nem altera banco de dados quando já tem um nome igual"""
        self.client.get(reverse("search-people", args=["Luke"]))
        response = [i.mass for i in self.data]
        self.assertEqual(len(self.data), 1)
        self.assertIn("xxxx", response)

    # def test_para_não_poder_ter_nome_repetido(self):
    #     """Teste que verifica se não tem como inserir 2 nomes iguais no banco de dados"""
    #     self.people2 = People.objects.create(name="Luke Skywalker", height="172", mass="77", hair_color="blond",
    #     skin_color="fair", eye_color="blue", birth_year="19BBY", gender="male", homeworld="https://swapi.dev/api/planets/1/")
    #     self.assertRaises(FooException, self.people2)
