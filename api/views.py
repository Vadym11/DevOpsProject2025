from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer


# Book resource
# /api/books
# Create your views here.

class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "status": "ok",
                "running": "yes"
            }
        )

health_view = HealthView.as_view()

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(
            {
                "test": "ok"
            }
        )

test_view = TestView.as_view()


# class BookView(APIView):
#     def get(self, request, *args, **kwargs):
#         return Response(
#             {
#                 "hello": "django"
#             }
#         )


#
# /api/books - All methods (GET, POST)
#
class BookView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = BookSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Book.objects.create()
        # alternatively
        # if not serializer.is_valid():
        #     error_response = {"errors": serializer.errors}
        #     return Response(error_response, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data)

book_view = BookView.as_view()

class BookDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

book_detail_view = BookDetailView.as_view()

