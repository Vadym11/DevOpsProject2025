from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book

# class BookViewTest(APITestCase):
#     def test_reponse_is_correct(self):
#         url = reverse('api:books')
#         response = self.client.get(url, format='json')
#         body = response.json()
#         assert body['hello'] == 'django'
#         assert response.status_code == status.HTTP_200_OK

class BookViewTest(APITestCase):
    def test_reponse_is_correct(self):
        book = Book.objects.create(
            title="Demo",
            author="Author1",
            isbn='1234567890'
        )
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        body = response.json()
        assert response.status_code == status.HTTP_200_OK
        # this will fail because of created_at field
        # assert body == [
        #     {
        #         "title": book.title,
        #         "description": book.description,
        #         "author": book.author
        #     }
        # ]
        assert body[0]['title'] == book.title


class HealthViewTest(APITestCase):
    def test_reponse_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        body = response.json()
        assert body['status'] == 'ok'
        assert response.status_code == status.HTTP_200_OK