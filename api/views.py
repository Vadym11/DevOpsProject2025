from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Book resource
# /api/books
# Create your views here.

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "status": "ok"
            }
        )


class BookView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "hello": "django"
            }
        )

book_view = BookView.as_view()

health_view = HealthView.as_view()

