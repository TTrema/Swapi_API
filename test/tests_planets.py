from rest_framework.test import APITestCase
from swapi.models import Planet
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase):
    def setUp(self):
        self.list_url = reverse("planets-list")

    def test_requisicao_get_para_listar_os_planetas(self):
        """Test para verificar a requisição GET para listar os planetas"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
