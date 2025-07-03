from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class BookViewTest(APITestCase):
    def test_reponse_is_correct(self):
        # 200 =< 300
        # 400 =< 500
        # 500
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        body = response.json()
        assert body['hello'] == 'django'
        assert response.status_code == status.HTTP_200_OK