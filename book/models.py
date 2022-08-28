from django.db import models

from genre.models import Genre
from reader.models import Reader

class Book(models.Model):
    bid = models.CharField(max_length=13,primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    photo_url = models.CharField(max_length=255)
    page_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    genres = models.ManyToManyField(Genre)
    authors = models.ManyToManyField(Reader, related_name='authored_books')

    class Meta:
        db_table = 'book'
        
    def __str__(self):
        return str({
            'bid': self.bid,
            'title': self.title,
            'description': self.description,
            'photo_url': self.photo_url,
            'page_count': self.page_count,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'genres': self.genres.all(),
            'authors': self.authors.all(),
        })
    