from datetime import date

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book

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
        assert body[0]['title'] == book.title

    def test_create_book_success(self):
        payload = {
            "title": "New Book",
            "author": "Jane Doe",
            "isbn": "9781234567897",
            "published_date": "2024-08-01"
        }
        url = reverse('api:books')
        resp = self.client.post(url, payload, format='json')
        assert resp.status_code == status.HTTP_200_OK
        body = resp.json()
        assert body["title"] == payload["title"]
        assert body["author"] == payload["author"]
        assert body["isbn"] == payload["isbn"]
        assert "id" in body

    def test_create_book_missing_required_fields(self):
        payload = {}
        url = reverse('api:books')
        resp = self.client.post(url, payload, format='json')
        assert resp.status_code == status.HTTP_400_BAD_REQUEST
        body = resp.json()
        assert body["title"] == ['This field is required.']
        assert body["author"] == ['This field is required.']

class HealthViewTest(APITestCase):
    def test_reponse_is_correct(self):
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        body = response.json()
        assert body['status'] == 'ok'
        assert response.status_code == status.HTTP_200_OK