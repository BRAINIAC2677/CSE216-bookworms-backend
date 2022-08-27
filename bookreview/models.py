from django.db import models

from reader.models import Reader
from book.models import Book

class BookReview(models.Model):
    brid = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reader, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    content = models.TextField(default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    loved_by = models.ManyToManyField(Reader, related_name='loved_bookreviews')

    class Meta:
        db_table = 'book_review'

    def __str__(self):
        return str({
            'brid': self.brid,
            'book': self.book,
            'reviewer': self.reviewer,
            'rating': self.rating,
            'content': self.content,    
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'loved_by': self.loved_by
        })

