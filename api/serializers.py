from rest_framework import serializers
from .models import Book

# use this if want to specify fields manually
# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author', 'created_at']