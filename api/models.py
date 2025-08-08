from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, default='1234567890')
    published_date = models.DateField(default='2000-01-01')
    created_at = models.DateTimeField(auto_now_add=True)

    # print Book instance in a nice way
    def __str__(self):
        return f"{self.title} by {self.author}"