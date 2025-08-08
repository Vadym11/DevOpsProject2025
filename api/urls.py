from django.urls import re_path
from .views import book_view, book_detail_view, health_view, test_view

app_name = 'api'

urlpatterns = [
    re_path(
        r"^books/?$", book_view, name='books'
    ),
    re_path(
        r"^books/(?P<pk>\d+)/$", book_detail_view, name="book-specific"
    ),
    re_path(
        r"^books/?$", book_detail_view, name="books-update"
    ),
    re_path(
        r"^test/", test_view, name='test'
    ),
    re_path(
        "", health_view, name='health'
    )
]