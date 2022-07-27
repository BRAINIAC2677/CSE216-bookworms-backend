from django.db import models

from genre.models import Genre
from reader.models import Reader

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=13,primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo_url = models.CharField(max_length=255)
    page_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Reader)

    def __str__(self):
        return self.title