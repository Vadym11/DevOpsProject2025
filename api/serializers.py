from rest_framework import serializers
from .models import Book

# use this if want to specify fields manually
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'published_date', 'created_at']
        read_only_fields = ['id', 'created_at']